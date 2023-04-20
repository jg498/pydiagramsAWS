from diagrams import Cluster, Diagram
from diagrams.aws.analytics import Kinesis, DataExchange, LakeFormation, Athena, Glue ,EMRCluster, Quicksight 
from diagrams.aws.network import  VPC
from diagrams.aws.storage import S3
from diagrams.aws.iot import IotSensor
from diagrams.aws.general import GenericDatabase

with Diagram("AWS Data Lake Architecture", show=True):
    with Cluster("IoT Sensors"):
        sensor = IotSensor("IoT\nSensor")

    with Cluster("On-Premises Data"):
        database = GenericDatabase("Database")

    
    with Cluster("Third-Party Data"):
        dataexchange = DataExchange("Data\nExchange") 


    with Cluster("Data Ingestion"):    
        kinesis = Kinesis("Kinesis\nData Streams")

    with Cluster("Data Lake"):
        lake = LakeFormation("Lake\nFormation")

    with Cluster("Data Lake"):
        s3 = S3("S3\nBucket")

    with Cluster("Data Lake Transformation"):
        glue = Glue("Glue") 
    
    with Cluster("Data Lake Transformation"):
        emr = EMRCluster("EMR\nCluster") 
    
    with Cluster("Data Lake Transformation"):
        s32= S3("S3\nTransformation Bucket")
       
    with Cluster(" Data Lake Visualization"): 
        athena = Athena("Athena") 

    with Cluster(" Data Lake Visualization"): 
        quicksight = Quicksight("Quicksight")



    with Cluster("Network"):
        vpc = VPC("VPC")


    # Create edges between the nodes
    sensor >> kinesis >> lake >> s3
    database >> kinesis 
    dataexchange >> kinesis 
    s3 >> glue 
    s3 >> emr 
    emr >> s32
    glue >> s32  
    s32 >> athena 
    athena >> quicksight

    
    # Set the direction of the graph to left-to-right
    Diagram(direction="LR")