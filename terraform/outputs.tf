output "vpc_id" {
  value = aws_vpc.myvpc.id
}

output "subnet_01_id" {
  value = aws_subnet.Mysubnet01.id
}

output "subnet_02_id" {
  value = aws_subnet.Mysubnet02.id
}

output "igw_id" {
  value = aws_internet_gateway.myigw.id
}

output "eks_cluster_name" {
  value = aws_eks_cluster.eks.name
}
