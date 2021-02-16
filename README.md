# lambda_eventbridge_demo

## Table of Contents
1. <a href="#introduction">designer</a>

2. <a href="#identity-access-management-iam">Identity Access Management (IAM)</a>

3. <a href="#simple-storage-service-s3">Simple Storage Service (S3)</a>

4. <a href="#cloudfront">CloudFront</a>

5. <a href="#snowball">Snowball</a>


## lambda function and execution result

![image](https://user-images.githubusercontent.com/32722949/108004583-45305280-6fc4-11eb-90fe-416a83184241.png)

## Identity Access Management (IAM)

### IAM Simplified:

IAM offers a centralized hub of control within AWS and integrates with all other AWS Services. IAM comes with the ability to share access at various levels of permission and it supports the ability to use identity federation (the process of delegating authentication to a trusted external party like Facebook or Google) for temporary or limited access. IAM comes with MFA support and allows you to set up custom password rotation policy across your entire organization. 
It is also PCI DSS compliant i.e. payment card industry data security standard. (passes government mandated credit card security regulations).

![image](https://user-images.githubusercontent.com/32722949/108004645-67c26b80-6fc4-11eb-87c6-cd5a8332b168.png)


## Simple Storage Service (S3)

### S3 Simplified:
S3 provides developers and IT teams with secure, durable, and highly-scalable object storage. Object storage, as opposed to block storage, is a general term that refers to data composed of three things:

  1.) the data that you want to store

  2.) an expandable amount of metadata

  3.) a unique identifier so that the data can be retrieved 

This makes it a perfect candidate to host files or directories and a poor candidate to host databases or operating systems. The following table highlights key differences between object and block storage:

![image](https://user-images.githubusercontent.com/32722949/107996192-ccbe9700-6fad-11eb-9fab-d7daadc64a0f.png)
