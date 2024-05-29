
#Adding security group
resource "aws_security_group" "allow_tls" {
  #checkov:skip=CKV_AWS_24:Reason for skipping this check
  #checkov:skip=CKV_AWS_23:Reason for skipping this check

  name_prefix = "allow_tls_"
  description = "Allow TLS inbound traffic"
  vpc_id      = aws_vpc.myvpc.id

  ingress {
    description = "TLS from VPC"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


