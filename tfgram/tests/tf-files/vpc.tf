module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "medgrupo-us"
  cidr = "10.150.0.0/16"

  azs             = ["us-east-1a", "us-east-1b", "us-east-1c", "us-east-1d", "us-east-1e"]
  private_subnets = ["10.150.0.0/24", "10.150.1.0/24", "10.150.2.0/24", "10.150.3.0/24", "10.150.4.0/24"]
  public_subnets  = ["10.150.5.0/24", "10.150.6.0/24", "10.150.7.0/24", "10.150.8.0/24", "10.150.9.0/24"]

  enable_nat_gateway = true
  enable_vpn_gateway = true
  enable_dns_hostnames = true

  tags = {
    Terraform = "true"
  }
}
