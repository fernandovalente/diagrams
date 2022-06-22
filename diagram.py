from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EB, EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, Route53
from diagrams.aws.storage import S3
from diagrams.aws.security import ACM


with Diagram("Greenole", show=False):
    dns = Route53("DNS")
    lb = ELB("Load Balance")
    acm = ACM("CertificateManager")
    ec2 = EC2("EC2")
    s3 = S3("S3")
    rds = RDS("DB PostgresSQL")

    # EC2
    ec2 >> acm
    ec2 >> s3
    dns >> lb >> ec2 >> rds
