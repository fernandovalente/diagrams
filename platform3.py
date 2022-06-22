from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EB, EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, Route53
from diagrams.aws.storage import S3
from diagrams.aws.security import ACM


with Diagram("Greenole", show=False):
    # Plat 3.0
    dns_plat3 = Route53("DNS")
    lb_plat3 = ELB("Load Balance")
    acm_plat3 = ACM("CertificateManager")
    ec2_plat3 = EC2("EC2")
    s3_plat3 = S3("S3")
    rds_plat3 = RDS("DB PostgresSQL")

    # Diagram
    ec2_plat3 >> acm_plat3
    ec2_plat3 >> s3_plat3
    dns_plat3 >> lb_plat3 >> ec2_plat3 >> rds_plat3

    # API Device
    lb_api_device = ELB("Load Balance")

    lb_api_device >> dns_plat3