from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, InternetGateway, VPC
from diagrams.aws.network import PublicSubnet, PrivateSubnet
from diagrams.aws.analytics import EMR, Athena
from diagrams.aws.storage import S3

with Diagram("Three-Tier-Architecture-diagrams-py", show=True):
    with Cluster("Frontend"):
            frontend = EC2("EC2")
    
    with Cluster("Load Balancer"):
        elb = ELB("ELB")

    with Cluster("Backend"):
        backend = EC2("EC2")
        database = RDS("RDS")

    with Cluster("Analytics"):
        emr = EMR("EMR")
        s3 = S3("S3")
        athena = Athena("Athena")

    with Cluster("VPC"):
        igw = InternetGateway("IGW")

        with Cluster("Public Subnet"):
            public_subnet = PublicSubnet("Public Subnet")

            

        with Cluster("Private Subnet"):
            private_subnet = PrivateSubnet("Private Subnet")


    with Cluster("Internal"):
        internal = VPC("Internal")
    
    internal >> frontend
    internal >>backend

    
    igw >> public_subnet
    igw >> private_subnet
    public_subnet >> frontend >> elb
    private_subnet >> backend >> elb >> database
    

    emr >> s3
    s3 >> athena
    igw >> elb
    



