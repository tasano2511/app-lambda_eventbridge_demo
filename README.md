# lambda_eventbridge_demo

## Table of Contents
1. <a href="#introduction">Introduction</a>

2. <a href="#identity-access-management-iam">Identity Access Management (IAM)</a>

3. <a href="#simple-storage-service-s3">Simple Storage Service (S3)</a>

4. <a href="#cloudfront">CloudFront</a>

5. <a href="#snowball">Snowball</a>


## Introduction

<a href="https://d1.awsstatic.com/training-and-certification/docs-sa-assoc/AWS-Certified-Solutions-Architect-Associate-Exam-Guide_v1.1_2019_08_27_FINAL.pdf">**The official AWS Solutions Architect - Associate (SAA-C02) exam guide**</a>

### Exam Content Breakdown:
![Screen Shot 2020-06-05 at 2 49 08 PM](https://user-images.githubusercontent.com/13093517/83912374-c2b87900-a73b-11ea-9691-b38383b43ff9.png)

new screen added>
![GitHub Logo](https://github.com/tasano2511/lambda_eventbridge_demo/blob/main/test.PNG)

2nd image added>
![image](https://user-images.githubusercontent.com/32722949/107996192-ccbe9700-6fad-11eb-9fab-d7daadc64a0f.png)

*Domain 1: Design Resilient Architectures*

  1.1 - Design a multi-tier architecture solution

  1.2 - Design highly available and/or fault-tolerant architectures

  1.3 - Design decoupling mechanisms using AWS services

  1.4 - Choose appropriate resilient storage


*Domain 2: Design High-Performing Architectures*

  2.1 - Identify elastic and scalable **compute** solutions for a workload

  2.2 - Select high-performing and scalable **storage** solutions for a workload

  2.3 - Select high-performing **networking** solutions for a workload

  2.4 - Choose high-performing **database** solutions for a workload


*Domain 3: Design Secure Applications and Architectures*

  3.1 - Design secure access to AWS resources

  3.2 - Design secure application tiers

  3.3 - Select appropriate data security options


*Domain 4: Design Cost-Optimized Architectures*

  4.1 - Identify cost-effective **storage** solutions

  4.2 - Identify cost-effective **compute** and **database** services

  4.3 - Design cost-optimized **network** architectures



## Identity Access Management (IAM)

### IAM Simplified:

IAM offers a centralized hub of control within AWS and integrates with all other AWS Services. IAM comes with the ability to share access at various levels of permission and it supports the ability to use identity federation (the process of delegating authentication to a trusted external party like Facebook or Google) for temporary or limited access. IAM comes with MFA support and allows you to set up custom password rotation policy across your entire organization. 
It is also PCI DSS compliant i.e. payment card industry data security standard. (passes government mandated credit card security regulations).

### IAM Entities:

**Users** - any individual end user such as an employee, system architect, CTO, etc.

**Groups** - any collection of similar people with shared permissions such as system administrators, HR employees, finance teams, etc. Each user within their specified group will inherit the permissions set for the group.

**Roles** - any software service that needs to be granted permissions to do its job, e.g- AWS Lambda needing write permissions to S3 or a fleet of EC2 instances needing read permissions from a RDS MySQL database.

**Policies** - the documented rule sets that are applied to grant or limit access. In order for users, groups, or roles to properly set permissions, they use policies. Policies are written in JSON and you can either use custom policies for your specific needs or use the default policies set by AWS.

![Screen Shot 2020-06-06 at 10 49 48 PM](https://user-images.githubusercontent.com/13093517/83959193-11533980-a848-11ea-9d03-d8133e0aaa86.png)

IAM Policies are separated from the other entities above because they are not an IAM Identity. Instead, they are attached to IAM Identities so that the IAM Identity in question can perform its necessary function.


## Simple Storage Service (S3)

### S3 Simplified:
S3 provides developers and IT teams with secure, durable, and highly-scalable object storage. Object storage, as opposed to block storage, is a general term that refers to data composed of three things:

  1.) the data that you want to store

  2.) an expandable amount of metadata

  3.) a unique identifier so that the data can be retrieved 

This makes it a perfect candidate to host files or directories and a poor candidate to host databases or operating systems. The following table highlights key differences between object and block storage:

![Screen Shot 2020-06-05 at 3 34 57 PM](https://user-images.githubusercontent.com/13093517/83915925-352c5780-a742-11ea-975b-53d4e5d07e7c.png)


Data uploaded into S3 is spread across multiple files and facilities. The files uploaded into S3 have an upper-bound of 5TB per file and the number of files that can be uploaded is virtually limitless. S3 buckets, which contain all files, are named in a universal namespace so uniqueness is required. All successful uploads will return an HTTP 200 response.


## CloudFront

### CloudFront Simplified:
The AWS CDN service is called CloudFront. It serves up cached content and assets for the increased global performance of your application. The main components of CloudFront are the edge locations (cache endpoints), the origin (original source of truth to be cached such as an EC2 instance, an S3 bucket, an Elastic Load Balancer or a Route 53 config), and the distribution (the arrangement of edge locations from the origin or basically the network itself). <a href="https://aws.amazon.com/cloudfront/features/">More info on CloudFront's features</a>

### CloudFront Key Details:
- When content is cached, it is done for a certain time limit called the Time To Live, or TTL, which is always in seconds
- If needed, CloudFront can serve up entire websites including dynamic, static, streaming and interactive content. 
- Requests are always routed and cached in the nearest edge location for the user, thus propagating the CDN nodes and guaranteeing best performance for future requests.
- There are two different types of distributions: 
  - **Web Distribution**: web sites, normal cached items, etc
  - **RTMP**: streaming content, adobe, etc
- Edge locations are not just read only. They can be written to which will then return the write value back to the origin.
- Cached content can be manually invalidated or cleared beyond the TTL, but this does incur a cost.
- You can invalidate the distribution of certain objects or entire directories so that content is loaded directly from the origin every time. Invalidating content is also helpful when debugging if content pulled from the origin seems correct, but pulling that same content from an edge location seems incorrect.
- You can set up a failover for the origin by creating an origin group with two origins inside. One origin will act as the primary and the other as the secondary. CloudFront will automatically switch between the two when the primary origin fails.
- Amazon CloudFront delivers your content from each edge location and offers a Dedicated IP Custom SSL feature. SNI Custom SSL works with most modern browsers.
- If you run PCI or HIPAA-compliant workloads and need to log usage data, you can do the following:
    - Enable CloudFront access logs. 
    - Capture requests that are sent to the CloudFront API.
- An Origin Access Identity (OAI) is used for sharing private content via CloudFront. The OAI is a virtual user that will be used to give your CloudFront distribution permission to fetch a private object from your origin (e.g. S3 bucket).

### CloudFront Signed URLs and Signed Cookies:
- CloudFront signed URLs and signed cookies provide the same basic functionality: they allow you to control who can access your content. These features exist because many companies that distribute content via the internet want to restrict access to documents, business data, media streams, or content that is intended for selected users. As an example, users who have paid a fee should be able to access private content that users on the free tier shouldn't. 
- If you want to serve private content through CloudFront and you're trying to decide whether to use signed URLs or signed cookies, consider the following:
  - Use signed URLs for the following cases:
    - You want to use an RTMP distribution. Signed cookies aren't supported for RTMP distributions.
    - You want to restrict access to individual files, for example, an installation download for your application.
    - Your users are using a client (for example, a custom HTTP client) that doesn't support cookies.
  - Use signed cookies for the following cases:
    - You want to provide access to multiple restricted files. For example, all of the files for a video in HLS format or all of the files in the paid users' area of a website.
    - You don't want to change your current URLs.

## Snowball

### Snowball Simplified:
Snowball is a giant physical disk that is used for migrating high quantities of data into AWS. It is a peta-byte scale data transport solution. Using a large disk like Snowball helps to circumvent common large scale data transfer problems such as high network costs, long transfer times, and security concerns. Snowballs are extremely secure by design and once the data transfer is complete, the snowballs are wiped clean of your data.

### Snowball Key Details:
- Snowball is a strong choice for a data transfer job if you need a secure and quick data transfer ranging in the terabytes to many petabytes into AWS. 
- Snowball can also be the right choice if you don’t want to make expensive upgrades to your existing network infrastructure, if you frequently experience large backlogs of data, if you're located in a physically isolated environment, or if you're in an area where high-speed internet connections are not available or cost-prohibitive.
- As a rule of thumb, if it takes more than one week to upload your data to AWS using the spare capacity of your existing internet connection, then you should consider using Snowball. 
- For example, if you have a 100 Mb connection that you can solely dedicate to transferring your data and you need to transfer 100 TB of data in total, it will take more than 100 days for the transfer to complete over that connection. You can make the same transfer in about a week by using multiple Snowballs.
- Here is a reference for when Snowball should be considered based on the number of days it would take to make the same transfer over an internet connection:

![Screen Shot 2020-06-07 at 10 53 22 PM](https://user-images.githubusercontent.com/13093517/83988618-c271d680-a911-11ea-9594-a82f690a786b.png)


### Snowball Edge and Snowmobile:
- Snowball Edge is a specific type of Snowball that comes with both compute *and* storage capabilities via AWS Lambda and specific EC2 instance types. This means you can run code within your snowball while your data is en route to an Amazon data center. This enables support of local workloads in remote or offline locations and as a result, Snowball Edge does not need to be limited to a data transfer service. An interesting use case is with airliners. Planes sometimes fly with snowball edges onboard so they can store large amounts of flight data and compute necessary functions for the plane’s own systems. Snowball Edges can also be clustered locally for even better performance.
- Snowmobile is an exabyte-scale data transfer solution. It is a data transport solution for 100 petabytes of data and is contained within a 45-foot shipping container hauled by a semi-truck. This massive transfer makes sense if you want to move your entire data center with years of data into the cloud.

