# -*- coding: utf-8 -*-

import os, datetime, random, string

from django.contrib.auth.mixins     import LoginRequiredMixin
from django.utils.translation       import ugettext_lazy as _
from django.views.generic           import View
from django.http                    import HttpResponse, Http404, HttpResponseNotAllowed
from django.conf                    import settings

from io                             import BytesIO
from PyPDF2                         import PdfFileWriter, PdfFileReader, PdfFileMerger
from reportlab.lib                  import colors
from reportlab.pdfgen               import canvas
from reportlab.pdfbase              import pdfmetrics
from reportlab.pdfbase.pdfmetrics   import stringWidth
from reportlab.pdfbase.ttfonts      import TTFont
from reportlab.lib.pagesizes        import letter, landscape
from reportlab.lib.units            import inch, cm
from reportlab.lib.styles           import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus             import Paragraph, SimpleDocTemplate, Frame, FrameBreak, PageTemplate, Table, TableStyle

from unidecode                      import unidecode

from muayene.models                 import Muayene, Recete, Rapor, LaboratuvarIstek

class PrintMixin(object):
    """
    A mixin used by all PrintViews.
    """

    model = None
    font = None
    queryset = None

    def get_queryset(self):
        if self.queryset is None:
            if self.model:
                return self.model._default_manager.all()
            else:
                raise ImproperlyConfigured("%(cls) is missing a QuerySet. Define %(cls)s.model" % {'cls': self.__class__.__name__})

        return self.queryset.all()

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')

        if queryset is None:
            queryset = self.get_queryset()
        
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        else:
            raise AttributeError("Print View must be called with pk!")

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") % {'verbose_name': queryset.model._meta.verbose_name}) 
            
        return obj

    def register_font(self):
        font = os.path.join(settings.STATIC_ROOT, "fonts/pfs.ttf")

        pdfmetrics.registerFont(TTFont("PFS", font))

class RecetePrintView(PrintMixin, LoginRequiredMixin, View):
    login_url = '/login/'
    model = Recete

    def get(self, request, *args, **kwargs):
        recete = self.get_object()

        ad = str(recete.hasta.ad)
        soyad = str(recete.hasta.soyad)
        pk = str(recete.id)
        muayene_tarihi = str(recete.tarih)

        title = unidecode("%s-%s-recete-%s-%s" % (ad, soyad, pk, muayene_tarihi))
        filename = title + ".pdf"

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename=%s' % filename

        buff = BytesIO()

        doc = SimpleDocTemplate(buff, 
                                pagesize=letter, 
                                title=title, 
                                author="Dr. Ziya T. Güneş",
                                rightMargin=inch/4,
                                leftMargin=inch/4,
                                topMargin=inch/2,
                                bottomMargin=inch/4,
                                showBoundary=0)

        frame1 = Frame(doc.leftMargin,
                       doc.bottomMargin, 
                       doc.width, 
                       doc.height / 8, 
                       id="footer")
        frame2 = Frame(doc.leftMargin, 
                       doc.bottomMargin + doc.height / 8 + 6, 
                       doc.width, 
                       doc.height * 6 / 8, 
                       id="body")
        frame3 = Frame(doc.leftMargin, 
                       doc.bottomMargin + doc.height * 7 / 8 + 12, 
                       doc.width * 3 / 4 - 6, 
                       doc.height / 8, 
                       id="header_right")
        frame4 = Frame(doc.leftMargin + doc.width * 3 / 4 + 6, 
                       doc.bottomMargin + doc.height * 7 / 8 + 12, 
                       doc.width / 4 - 6, 
                       doc.height / 8, 
                       id="header_left")

        receteTemplate = PageTemplate(frames=[frame1, frame2, frame3, frame4])
        doc.addPageTemplates(receteTemplate)

        self.register_font()
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name="footer", fontName="PFS", fontSize=10, alignment=2, leading=20))
        styles.add(ParagraphStyle(name="heading", fontName="PFS", fontSize=20, alignment=0, spaceAfter=40))
        styles.add(ParagraphStyle(name="ilac_ad", fontName="PFS", fontSize=14, alignment=0, leftIndent=30, spaceAfter=10, leading=20))
        styles.add(ParagraphStyle(name="ilac_kullanim", fontName="PFS", fontSize=12, alignment=0, leftIndent=50, spaceAfter=20, leading=20))
        styles.add(ParagraphStyle(name="header_left", fontName="PFS", fontSize=12, alignment=0))
        styles.add(ParagraphStyle(name="header_right", fontName="PFS", fontSize=12, alignment=2))

        story = []

        ad = Paragraph("Dr. Ziya T. GÜNEŞ", styles['footer'])
        tel = Paragraph("0(232) 422 00 56", styles['footer'])
        mail = Paragraph("info@ziyagunes.com", styles['footer'])
        adres = Paragraph("Işılay Saygın Sokak No:17 Kat:2 Alsancak/İzmir", styles['footer'])

        story.append(ad)
        story.append(tel)
        story.append(mail)
        story.append(adres)

        story.append(FrameBreak())

        heading = Paragraph("R<u>p/</u>", styles['heading'])

        story.append(heading)

        ilac1 = Paragraph("1. %s (%d kutu)" % (recete.ilac1.ad, recete.ilac1_kutu), styles['ilac_ad'])
        ilac1_kullanim = Paragraph("S: %s" % (recete.ilac1_kullanim), styles['ilac_kullanim'])
        story.append(ilac1)
        story.append(ilac1_kullanim)

        if recete.ilac2:
            ilac2 = Paragraph("2. %s (%d kutu)" % (recete.ilac2.ad, recete.ilac2_kutu), styles['ilac_ad'])
            ilac2_kullanim = Paragraph("S: %s" % (recete.ilac2_kullanim), styles['ilac_kullanim'])
            story.append(ilac2)
            story.append(ilac2_kullanim)

        if recete.ilac3:
            ilac3 = Paragraph("3. %s (%d kutu)" % (recete.ilac3.ad, recete.ilac3_kutu), styles['ilac_ad'])
            ilac3_kullanim = Paragraph("S: %s" % (recete.ilac3_kullanim), styles['ilac_kullanim'])
            story.append(ilac3)
            story.append(ilac3_kullanim)
        
        if recete.ilac4:
            ilac4 = Paragraph("4. %s (%d kutu)" % (recete.ilac4.ad, recete.ilac4_kutu), styles['ilac_ad'])
            ilac4_kullanim = Paragraph("S: %s" % (recete.ilac4_kullanim), styles['ilac_kullanim'])
            story.append(ilac4)
            story.append(ilac4_kullanim)

        if recete.ilac5:
            ilac5 = Paragraph("5. %s (%d kutu)" % (recete.ilac5.ad, recete.ilac5_kutu), styles['ilac_ad'])
            ilac5_kullanim = Paragraph("S: %s" % (recete.ilac5_kullanim), styles['ilac_kullanim'])
            story.append(ilac5)
            story.append(ilac5_kullanim)

        story.append(FrameBreak())

        hasta = str(recete.hasta)
        hasta_paragraph = Paragraph(hasta, styles['header_left'])

        story.append(hasta_paragraph)

        story.append(FrameBreak())

        tarih_paragraph = Paragraph(muayene_tarihi, styles['header_right'])

        story.append(tarih_paragraph)

        doc.build(story)

        response.write(buff.getvalue())
        buff.close()

        return response

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

class RaporPrintView(PrintMixin, LoginRequiredMixin, View):
    login_url = '/login/'
    model = Rapor

    def get(self, request, *args, **kwargs):
        rapor = self.get_object()

        ad = str(rapor.hasta.ad)
        soyad = str(rapor.hasta.soyad)
        pk = str(rapor.id)
        muayene_tarihi = str(rapor.tarih)

        title = unidecode("%s-%s-rapor-%s-%s" % (ad, soyad, pk, muayene_tarihi))
        filename = title + ".pdf"

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename=%s' % filename

        buff = BytesIO()

        doc = SimpleDocTemplate(buff, 
                                pagesize=letter, 
                                title=title, 
                                author="Dr. Ziya T. Güneş", 
                                topMargin=inch/2,
                                bottomMargin=inch/4,
                                leftMargin=inch/4,
                                rightMargin=inch/4)

        frame1 = Frame(doc.leftMargin,
                       doc.bottomMargin, 
                       doc.width, 
                       doc.height / 8, 
                       id="footer")
        frame2 = Frame(doc.leftMargin, 
                       doc.bottomMargin + doc.height / 8 + 6, 
                       doc.width, 
                       doc.height * 6 / 8, 
                       id="body")
        frame3 = Frame(doc.leftMargin,
                       doc.bottomMargin + doc.height * 7 / 8 + 6,
                       doc.width,
                       doc.height / 8,
                       id="header")

        receteTemplate = PageTemplate(frames=[frame1, frame2,frame3])
        doc.addPageTemplates(receteTemplate)

        self.register_font()

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name="centered", alignment=1, fontName="PFS", fontSize=24, spaceAfter=30)) 
        styles.add(ParagraphStyle(name="body", fontName="PFS", fontSize=12, leading=20))
        styles.add(ParagraphStyle(name="footer", fontName="PFS", fontSize=10, leading=20, alignment=2))
        styleH = styles['centered'] 
        styleB = styles['body']
        styleF = styles['footer']

        story = []

        dogum_tarihi = str(rapor.hasta.dogum_tarihi)
        hasta = str(rapor.hasta)
        tani = str(rapor.tani)
        gun = str(rapor.gun)

        heading = "RAPOR"
        body = "%s tarihinde başvuran, %s doğum tarihli %s'ın %s tanısı ile %s gün istirahati uygundur." % (muayene_tarihi, dogum_tarihi, hasta, tani, gun)
        tel = "0(232) 422 00 56"
        mail = "info@ziyagunes.com"
        adres = "Işılay Saygın Sokak No:17 Kat:2 Alsancak/İzmir"

        story.append(Paragraph(tel, styleF))
        story.append(Paragraph(mail, styleF))
        story.append(Paragraph(adres, styleF))

        story.append(FrameBreak())

        story.append(Paragraph(heading, styleH))
        story.append(Paragraph(body, styleB))

        doc.build(story)

        response.write(buff.getvalue())
        buff.close()

        return response

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

class LabIstekPrintView(PrintMixin, LoginRequiredMixin, View):
    login_url = '/login/'
    model = LaboratuvarIstek

    def get(self, request, *args, **kwargs):
        istek = self.get_object()

        muayene_tarihi = str(istek.tarih)
        ad = str(istek.hasta.ad)
        soyad = str(istek.hasta.soyad)
        pk = str(istek.pk)

        title = unidecode("%s-%s-istek-%s-%s" % (ad, soyad, pk, muayene_tarihi))
        filename = title + ".pdf"

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename=%s' % filename

        buff = BytesIO()

        doc = SimpleDocTemplate(buff, 
                                pagesize=letter, 
                                title=title, 
                                author="Dr. Ziya T. Güneş",
                                rightMargin=inch/4,
                                leftMargin=inch/4,
                                topMargin=inch/2,
                                bottomMargin=inch/4,
                                showBoundary=0)

        frame1 = Frame(doc.leftMargin,
                       doc.bottomMargin, 
                       doc.width, 
                       doc.height / 8, 
                       id="footer")
        frame2 = Frame(doc.leftMargin, 
                       doc.bottomMargin + doc.height / 8 + 6, 
                       doc.width, 
                       doc.height * 6 / 8, 
                       id="body")
        frame3 = Frame(doc.leftMargin, 
                       doc.bottomMargin + doc.height * 7 / 8 + 12, 
                       doc.width * 3 / 4 - 6, 
                       doc.height / 8, 
                       id="header_right")
        frame4 = Frame(doc.leftMargin + doc.width * 3 / 4 + 6, 
                       doc.bottomMargin + doc.height * 7 / 8 + 12, 
                       doc.width / 4 - 6, 
                       doc.height / 8, 
                       id="header_left")

        receteTemplate = PageTemplate(frames=[frame1, frame2, frame3, frame4])
        doc.addPageTemplates(receteTemplate)

        self.register_font()
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name="footer", fontName="PFS", fontSize=10, alignment=2, leading=20))
        styles.add(ParagraphStyle(name="heading", fontName="PFS", fontSize=16, alignment=1, spaceAfter=30))
        styles.add(ParagraphStyle(name="body", fontName="PFS", fontSize=10, alignment=0, leftIndent=30, spaceAfter=0, leading=20))
        styles.add(ParagraphStyle(name="header_left", fontName="PFS", fontSize=12, alignment=0))
        styles.add(ParagraphStyle(name="header_right", fontName="PFS", fontSize=12, alignment=2))

        story = []

        ad = Paragraph("Dr. Ziya T. GÜNEŞ", styles['footer'])
        tel = Paragraph("0(232) 422 00 56", styles['footer'])
        mail = Paragraph("info@ziyagunes.com", styles['footer'])
        adres = Paragraph("Işılay Saygın Sokak No:17 Kat:2 Alsancak/İzmir", styles['footer'])

        story.append(ad)
        story.append(tel)
        story.append(mail)
        story.append(adres)

        story.append(FrameBreak())

        heading = Paragraph("TETKİK İSTEM", styles['heading'])

        story.append(heading)

        for name in istek.get_true_fields():
            par1 = Paragraph("* %s" % (name), styles['body'])
            story.append(par1)
        
        story.append(FrameBreak())

        hasta = str(istek.hasta)
        hasta_paragraph = Paragraph(hasta, styles['header_left'])

        story.append(hasta_paragraph)

        story.append(FrameBreak())

        tarih_paragraph = Paragraph(muayene_tarihi, styles['header_right'])

        story.append(tarih_paragraph)

        doc.build(story)

        response.write(buff.getvalue())
        buff.close()

        return response

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

class TTFPrintView(PrintMixin, LoginRequiredMixin, View):
    login_url = '/login/'
    model = Muayene

    def get(self, request, *args, **kwargs):
        muayene = self.get_object()

        ad = str(muayene.hasta.ad)
        soyad = str(muayene.hasta.soyad)
        dogum_tarihi = str(muayene.hasta.dogum_tarihi)
        tc_kimlik_no = str(muayene.hasta.tc_kimlik_no)

        pk = str(muayene.pk)
        muayene_tarihi = str(muayene.tarih)
        yakinma = str(muayene.yakinma)
        baki = str(muayene.baki)
        tani = str(muayene.ontani_tani)
        kullandigi_ilaclar = str(muayene.kullandigi_ilaclar)

        tarih = str(datetime.date.today())

        title = unidecode("%s-%s-ttf-%s-%s" % (ad, soyad, pk, muayene_tarihi))
        filename = title + ".pdf"

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename=%s' % filename

        buff = BytesIO()

        self.register_font()

        can = canvas.Canvas(buff, pagesize=letter)
        can.setFont("PFS", 8)

        can.drawString(180, 710, ad + " " + soyad)
        can.drawString(181, 691, dogum_tarihi)
        can.drawString(181, 655, tc_kimlik_no)
        can.drawString(181, 605, muayene_tarihi)

        can.setFont("PFS", 7)

        yakinma_words = yakinma.split()
        leftovers = []
        yakinma_line1 = []
        yakinma_line2 = []
        yakinma_line3 = []
        line1_width = line2_width = line3_width = 0

        for word in yakinma_words:
            line1_width = stringWidth(' '.join(yakinma_line1), 'PFS', 7)
            if line1_width < 270:
                yakinma_line1.append(word)
            else:
                word_index = yakinma_words.index(word)
                leftovers = yakinma_words[word_index:]
                break

        if line1_width > 270:
            for word in leftovers:
                yakinma_line2.append(word)
                line2_width = stringWidth(' '.join(yakinma_line2), "PFS", 7)
                if line2_width > 500:
                    word_index = leftovers.index(word)
                    yakinma_line2 = leftovers[:word_index]
                    leftovers = leftovers[word_index:]
                    break

        if line2_width > 500:
            for word in leftovers:
                yakinma_line3.append(word)
                line3_width = stringWidth(' '.join(yakinma_line3), "PFS", 7)
                if line3_width > 500:
                    word_index = leftovers.index(word)
                    yakinma_line3 = yakinma_line2[:word_index]
                    leftovers = leftovers[word_index:]
                    break

        can.drawString(250, 513, ' '.join(yakinma_line1))
        can.drawString(70, 503, ' '.join(yakinma_line2))
        can.drawString(70, 493, ' '.join(yakinma_line3))

        ilaclar = kullandigi_ilaclar.split("/")
        ilaclar_line1 = []
        ilaclar_line2 = []

        for ilac in ilaclar:
            ilaclar_line1.append(ilac)
            width = stringWidth(','.join(ilaclar_line1), "PFS", 7)
            if width > 315:
                ilaclar_line2.append(ilaclar_line1.pop())

        ilac_line1 = ','.join(ilaclar_line1)
        ilac_line2 = ','.join(ilaclar_line2)

        can.drawString(250, 412, ilac_line1)
        can.drawString(60, 400, ilac_line2)

        baki_words = baki.split()
        leftovers = []
        baki_line1 = []
        baki_line2 = []
        baki_line3 = []
        line1_width = line2_width = line3_width = 0

        for word in baki_words:
            line1_width = stringWidth(' '.join(baki_line1), 'PFS', 7)
            if line1_width < 270:
                baki_line1.append(word)
            else:
                word_index = baki_words.index(word)
                leftovers = baki_words[word_index:]
                break

        if line1_width > 270:
            for word in leftovers:
                baki_line2.append(word)
                line2_width = stringWidth(' '.join(baki_line2), "PFS", 7)
                if line2_width > 500:
                    word_index = leftovers.index(word)
                    baki_line2 = leftovers[:word_index]
                    leftovers = leftovers[word_index:]
                    break

        if line2_width > 500:
            for word in leftovers:
                baki_line3.append(word)
                line3_width = stringWidth(' '.join(baki_line3), "PFS", 7)
                if line3_width > 500:
                    word_index = leftovers.index(word)
                    baki_line3 = leftovers[:word_index]
                    leftovers = leftovers[word_index:]
                    break

        can.drawString(250, 375, ' '.join(baki_line1))
        can.drawString(60, 360, ' '.join(baki_line2))
        can.drawString(60, 345, ' '.join(baki_line3))

        tani_words = tani.split()
        leftovers = []
        tani_line1 = []
        tani_line2 = []
        tani_line3 = []
        line1_width = line2_width = line3_width = 0

        for word in tani_words:
            line1_width = stringWidth(' '.join(tani_line1), 'PFS', 7)
            if line1_width < 90:
                tani_line1.append(word)
            else:
                word_index = tani_words.index(word)
                leftovers = tani_words[word_index:]
                break

        if line1_width > 90:
            for word in leftovers:
                tani_line2.append(word)
                line2_width = stringWidth(' '.join(tani_line2), "PFS", 7)
                if line2_width > 300:
                    word_index = leftovers.index(word)
                    tani_line2 = leftovers[:word_index]
                    leftovers = leftovers[word_index:]
                    break

        if line2_width > 300:
            for word in leftovers:
                tani_line3.append(word)
                line3_width = stringWidth(' '.join(tani_line3), "PFS", 7)
                if line3_width > 300:
                    word_index = leftovers.index(word)
                    tani_line3 = leftovers[:word_index]
                    leftovers = leftovers[word_index:]
                    break

        can.drawString(250, 280, ' '.join(tani_line1))
        can.drawString(60, 265, ' '.join(tani_line2))
        can.drawString(60, 245, ' '.join(tani_line3))

        yas = muayene.hasta.age() 
        if yas > 18:
            can.drawString(210, 47, ad + " " + soyad)

        can.drawString(120, 32, tarih)

        can.setTitle(title)

        can.save()

        buff.seek(0)

        ttf_filled = PdfFileReader(buff)
   
        FILE = os.path.join(settings.STATIC_ROOT, 'TTF.pdf')
        ttf_empty = PdfFileReader(open(FILE, "rb"))

        output = PdfFileWriter()

        page = ttf_empty.getPage(0)
        page.mergePage(ttf_filled.getPage(0))
        output.addPage(page)

        output.write(buff)
        response.write(buff.getvalue())
        buff.close()

        return response

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

class MultiTTFPrintView(PrintMixin, LoginRequiredMixin, View):
    login_url = '/login/'
    queryset = Muayene.objects.all()

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    def post(self, request, *args, **kwargs):
        start = request.POST.get('start', '')
        end = request.POST.get('end', '')

        qs = self.queryset.filter(tarih__gte=start,tarih__lte=end)

        self.register_font()

        files = []

        for muayene in qs:
            filename = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

            buff = BytesIO()
            can = canvas.Canvas(buff, pagesize=letter)

            ad = str(muayene.hasta.ad)
            soyad = str(muayene.hasta.soyad)
            dogum_tarihi = str(muayene.hasta.dogum_tarihi)
            tc_kimlik_no = str(muayene.hasta.tc_kimlik_no)

            pk = str(muayene.pk)
            muayene_tarihi = str(muayene.tarih)
            yakinma = str(muayene.yakinma)
            baki = str(muayene.baki)
            tani = str(muayene.ontani_tani)
            kullandigi_ilaclar = str(muayene.kullandigi_ilaclar)

            tarih = str(datetime.date.today())

            can.setFont("PFS", 8)

            can.drawString(180, 710, ad + " " + soyad)
            can.drawString(181, 691, dogum_tarihi)
            can.drawString(181, 655, tc_kimlik_no)
            can.drawString(181, 605, muayene_tarihi)

            can.setFont("PFS", 7)

            yakinma_words = yakinma.split()
            leftovers = []
            yakinma_line1 = []
            yakinma_line2 = []
            yakinma_line3 = []
            line1_width = line2_width = line3_width = 0

            for word in yakinma_words:
                line1_width = stringWidth(' '.join(yakinma_line1), 'PFS', 7)
                if line1_width < 270:
                    yakinma_line1.append(word)
                else:
                    word_index = yakinma_words.index(word)
                    leftovers = yakinma_words[word_index:]
                    break

            if line1_width > 270:
                for word in leftovers:
                    yakinma_line2.append(word)
                    line2_width = stringWidth(' '.join(yakinma_line2), "PFS", 7)
                    if line2_width > 500:
                        word_index = leftovers.index(word)
                        yakinma_line2 = leftovers[:word_index]
                        leftovers = leftovers[word_index:]
                        break

            if line2_width > 500:
                for word in leftovers:
                    yakinma_line3.append(word)
                    line3_width = stringWidth(' '.join(yakinma_line3), "PFS", 7)
                    if line3_width > 500:
                        word_index = leftovers.index(word)
                        yakinma_line3 = yakinma_line2[:word_index]
                        leftovers = leftovers[word_index:]
                        break

            can.drawString(250, 513, ' '.join(yakinma_line1))
            can.drawString(70, 503, ' '.join(yakinma_line2))
            can.drawString(70, 493, ' '.join(yakinma_line3))

            ilaclar = kullandigi_ilaclar.split("/")
            ilaclar_line1 = []
            ilaclar_line2 = []

            for ilac in ilaclar:
                ilaclar_line1.append(ilac)
                width = stringWidth(','.join(ilaclar_line1), "PFS", 7)
                if width > 315:
                    ilaclar_line2.append(ilaclar_line1.pop())

            ilac_line1 = ','.join(ilaclar_line1)
            ilac_line2 = ','.join(ilaclar_line2)

            can.drawString(250, 412, ilac_line1)
            can.drawString(60, 400, ilac_line2)

            baki_words = baki.split()
            leftovers = []
            baki_line1 = []
            baki_line2 = []
            baki_line3 = []
            line1_width = line2_width = line3_width = 0

            for word in baki_words:
                line1_width = stringWidth(' '.join(baki_line1), 'PFS', 7)
                if line1_width < 270:
                    baki_line1.append(word)
                else:
                    word_index = baki_words.index(word)
                    leftovers = baki_words[word_index:]
                    break

            if line1_width > 270:
                for word in leftovers:
                    baki_line2.append(word)
                    line2_width = stringWidth(' '.join(baki_line2), "PFS", 7)
                    if line2_width > 500:
                        word_index = leftovers.index(word)
                        baki_line2 = leftovers[:word_index]
                        leftovers = leftovers[word_index:]
                        break

            if line2_width > 500:
                for word in leftovers:
                    baki_line3.append(word)
                    line3_width = stringWidth(' '.join(baki_line3), "PFS", 7)
                    if line3_width > 500:
                        word_index = leftovers.index(word)
                        baki_line3 = leftovers[:word_index]
                        leftovers = leftovers[word_index:]
                        break

            can.drawString(250, 375, ' '.join(baki_line1))
            can.drawString(60, 360, ' '.join(baki_line2))
            can.drawString(60, 345, ' '.join(baki_line3))

            tani_words = tani.split()
            leftovers = []
            tani_line1 = []
            tani_line2 = []
            tani_line3 = []
            line1_width = line2_width = line3_width = 0

            for word in tani_words:
                line1_width = stringWidth(' '.join(tani_line1), 'PFS', 7)
                if line1_width < 90:
                    tani_line1.append(word)
                else:
                    word_index = tani_words.index(word)
                    leftovers = tani_words[word_index:]
                    break

            if line1_width > 90:
                for word in leftovers:
                    tani_line2.append(word)
                    line2_width = stringWidth(' '.join(tani_line2), "PFS", 7)
                    if line2_width > 300:
                        word_index = leftovers.index(word)
                        tani_line2 = leftovers[:word_index]
                        leftovers = leftovers[word_index:]
                        break

            if line2_width > 300:
                for word in leftovers:
                    tani_line3.append(word)
                    line3_width = stringWidth(' '.join(tani_line3), "PFS", 7)
                    if line3_width > 300:
                        word_index = leftovers.index(word)
                        tani_line3 = leftovers[:word_index]
                        leftovers = leftovers[word_index:]
                        break

            can.drawString(250, 280, ' '.join(tani_line1))
            can.drawString(60, 265, ' '.join(tani_line2))
            can.drawString(60, 245, ' '.join(tani_line3))

            yas = muayene.hasta.age() 
            if yas > 18:
                can.drawString(210, 47, ad + " " + soyad)

            can.drawString(120, 32, tarih)

            can.showPage()
            can.save()

            ttf_filled = PdfFileReader(buff)
            ttf_empty = PdfFileReader(open(os.path.join(settings.STATIC_ROOT, 'TTF.pdf'), "rb"))

            output = PdfFileWriter()

            page = ttf_empty.getPage(0)
            page.mergePage(ttf_filled.getPage(0))
            output.addPage(page)

            outputStream = open('/tmp/%s.pdf' % filename, 'wb')
            output.write(outputStream)
            outputStream.close()

            files.append('/tmp/%s.pdf' % filename)

        merger = PdfFileMerger()

        for f in files:
            merger.append(PdfFileReader(open(f, 'rb')))
            os.remove(f)

        start_date = str(start)
        end_date = str(end)

        title = unidecode("%s-%s-ttf" % (start_date, end_date))
        final_filename = title + ".pdf"

        merger.write("/tmp/%s" % final_filename)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename=%s' % final_filename

        pdf = open("/tmp/%s" % final_filename, 'rb').read()

        response.write(pdf)

        os.remove("/tmp/%s" % final_filename)

        return response

class AHSevkPrintView(PrintMixin, LoginRequiredMixin, View):
    login_url = '/login/'
    model = Muayene

    def get(self, request, *args, **kwargs):
        muayene = self.get_object()

        hasta = muayene.hasta
        ad = str(muayene.hasta.ad)
        soyad = str(muayene.hasta.soyad)
        tc_kimlik_no = str(muayene.hasta.tc_kimlik_no)
        yas = muayene.hasta.age()

        muayene_tarihi = str(muayene.tarih)
        pk = str(muayene.pk)

        title = unidecode("%s-%s-ahsevk-%s-%s" % (ad, soyad, pk, muayene_tarihi))
        filename = title + ".pdf"

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename=%s' % filename

        buff = BytesIO()

        self.register_font()

        can = canvas.Canvas(buff, pagesize=letter)

        can.setFont("PFS", 7)
        can.drawString(110, 750, str(muayene.hasta))

        can.setFont("PFS", 10)
        can.drawString(400, 715, tc_kimlik_no)

        if yas < 19:
            # Hemogram
            can.drawString(27, 660, 'X')
            # Sedim
            can.drawString(27, 646, 'X')
            # Tam İdrar
            can.drawString(27, 633, 'X')
        elif yas >= 19 and yas < 41:
            # Hemogram
            can.drawString(27, 660, 'X')
            # Sedim
            can.drawString(27, 646, 'X')
            # Tam İdrar
            can.drawString(27, 633, 'X')
            # Açlık Kan
            can.drawString(27, 619, 'X')
            # Total Kolesterol
            can.drawString(27, 606, 'X')
            # HDL Kolesterol
            can.drawString(27, 592, 'X')
            # Kreatinin
            can.drawString(27, 565, 'X')
            # SGOT
            can.drawString(27, 552, 'X')
            # SGPT
            can.drawString(27, 512, 'X')
            # EKG
            can.drawString(201, 660, 'X')
            # PA
            can.drawString(201, 646, 'X')
        elif yas >= 41:
            # Hemogram
            can.drawString(27, 660, 'X')
            # Sedim
            can.drawString(27, 646, 'X')
            # Tam İdrar
            can.drawString(27, 633, 'X')
            # Açlık Kan
            can.drawString(27, 619, 'X')
            # Total Kolesterol
            can.drawString(27, 606, 'X')
            # HDL Kolesterol
            can.drawString(27, 592, 'X')
            # LDL Kolesterol
            can.drawString(27, 579, 'X')
            # Kreatinin
            can.drawString(27, 565, 'X')
            # SGOT
            can.drawString(27, 552, 'X')
            # Ürik Asit
            can.drawString(27, 539, 'X')
            # SGPT
            can.drawString(27, 512, 'X')
            # EKG
            can.drawString(201, 660, 'X')
            # PA
            can.drawString(201, 646, 'X')

        can.drawString(90, 90, str(muayene.hasta))

        can.drawString(420, 72, str(muayene.tarih.day))
        can.drawString(450, 72, str(muayene.tarih.month))
        can.drawString(490, 72, str(muayene.tarih.strftime('%y')))

        can.setTitle(title)

        can.save()

        buff.seek(0)

        ah_filled = PdfFileReader(buff)

        FILE = os.path.join(settings.STATIC_ROOT, 'AH_ISTEK.pdf')
        ah_empty = PdfFileReader(open(FILE, "rb"))

        output = PdfFileWriter()

        page = ah_empty.getPage(0)
        page.mergePage(ah_filled.getPage(0))
        output.addPage(page)

        output.write(buff)
        response.write(buff.getvalue())
        buff.close()

        return response

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

class ListPrintView(PrintMixin, LoginRequiredMixin, View):
    login_url = '/login/'
    queryset = Muayene.objects.all()

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['GET'])

    def post(self, request, *args, **kwargs):
        start = request.POST.get('start', '')
        end = request.POST.get('end', '')

        qs = self.queryset.filter(tarih__gte=start,tarih__lte=end)

        title = '%s-%s-hasta-list' % (start, end)
        filename = title + ".pdf"

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename=%s' % filename

        buff = BytesIO()

        pdfmetrics.registerFont(TTFont('ListFont', '../fonts/listfont.ttf'))

        doc = SimpleDocTemplate(buff, 
                                pagesize=landscape(letter), 
                                title=title, 
                                author="Dr. Ziya T. Güneş",
                                rightMargin=inch/4,
                                leftMargin=inch/4,
                                topMargin=inch/2,
                                bottomMargin=inch/4,
                                showBoundary=0)

        story = []
        data = [['', 'TARİH', 'HASTA', 'TANI']]

        i = 0

        for muayene in qs:
            i += 1
            hasta = str(muayene.hasta) 
            tarih = str(muayene.tarih)
            tani = str(muayene.ontani_tani)
            
            row = ['%s' % i, tarih, hasta, tani]
            data.append(row)

        LIST_STYLE = TableStyle(
             [
                 ('FONT',           (0,0), (3,-1), 'ListFont', 8),
                 ('LEFTPADDING',    (0,0), (3,-1), 0.25*cm),
                 ('RIGHTPADDING',   (0,0), (3,-1), 0.25*cm),
             ]
         )

        table = Table(data)
        table.setStyle(LIST_STYLE)
        story.append(table)

        doc.build(story)

        response.write(buff.getvalue())
        buff.close()

        return response
