variable "do_token" {}
variable "ssh_password" {}

provider "digitalocean" {
    token = "${var.do_token}"
}

resource "digitalocean_droplet" "hastatakip" {
    image    = "40921535"
    name     = "hastatakip-1"
    region   = "fra1"
    size     = "s-1vcpu-2gb"
    ssh_keys = [16992631]

    provisioner "remote-exec" {
        inline = ["sudo su - hastatakip -c '/home/hastatakip/hastatakip/bin/restore.sh'"]

        connection {
            type = "ssh"
            user = "egegunes"
            password = "${var.ssh_password}"
        }
    }
}

resource "digitalocean_record" "hastatakip" {
    domain = "zygns.com"
    type   = "A"
    name   = "hastatakip"
    ttl    = 300
    value  = "${digitalocean_droplet.hastatakip.ipv4_address}"
}

resource "null_resource" "hastatakip" {
    connection {
        type = "ssh"
        host = "${digitalocean_droplet.hastatakip.ipv4_address}"
        user = "egegunes"
        password = "${var.ssh_password}"
    }

    provisioner "remote-exec" {
        inline = ["sudo certbot renew"]
    }
}
