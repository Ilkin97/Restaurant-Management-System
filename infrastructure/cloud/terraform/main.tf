provider "aws" {
  region = "eu-central-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-xxxxxxx"
  instance_type = "t2.micro"
}