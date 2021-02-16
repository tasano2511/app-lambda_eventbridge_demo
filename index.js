/*
simple lambda function that list buckets in s3
 - all pkgs must be defined outside of the handler
*/


// require the X-Ray SDK (need to install it first)
const AWSXRay = require('aws-xray-sdk');

// require the AWS SDK (comes with every lambda function)
const AWS = AWSXRay.captureAWS(require('aws-sdk'));

// We'll use the S3 service, so we need a proper IAM role
const s3 = new AWS.S3()

exports.handler = async function(event) {
    return s3.listBuckets().promise()
}
