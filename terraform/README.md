# NGINX Ingress Controller with EKS - ONLY for Weather-APP!!! AND Classic Load balancer type ):


# Create the EKS cluster - It will take a couple of minutes

terraform apply


# Connect to your cluster context 
aws eks update-kubeconfig --name <EKS-ClusterName> --region eu-north-1 --profile  <YOUR-AWS-USERNAME-Withpermissions>


# Install Ingress Controller

helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

helm install ingress-nginx ingress-nginx  --repo https://kubernetes.github.io/ingress-nginx  --namespace ingress-nginx  --create-namespace


# GO to your AWS in EC2 dashbourd find your new Load Balancer

    - copy the - Very long DNS name into the host in the values file


# Intall the helm Chart files
helm install <release-name>  .

# OR
helm install <release-name> /pathToFile/.tgz


# get the Load balancer ip address for the next step
curl -v <Verylong-AWS-DNS>

#check if the website is up 
curl --resolve www.<Verylong-AWS-DNS>:80:<LB-IP-ADD> http://<Verylong-AWS-DNS>


# visit your website in the browser using your Verylong-AWS-DNS




#refernce 

# terraform
https://medium.com/@sushantkapare1717/creating-aws-eks-cluster-using-terraform-b1a88d35829e

# NGINX Ingress Controller
https://amod-kadam.medium.com/setting-up-nginx-ingress-controller-with-eks-f27390bcf804




# Run test using terratest

go test -v -timeout 30m
