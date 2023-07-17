require 'aws-sdk-s3'
client = Aws::S3::Client.new(
    region: region_name,
    credentials: credentials,
    #
)