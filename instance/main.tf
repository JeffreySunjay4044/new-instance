data "aws_ami" "rhel" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

module amis {
  source  = "mamemomonga/linux-ami/aws"
}




resource "aws_instance" "web" {
  ami           = module.amis.debian.10.amd64
  instance_type = "t3.micro"

  tags = {
    owner = "sunjay@dqlabs.ai"
    env = "dev"
  }
}