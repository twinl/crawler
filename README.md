# TwiNL: crawler code

This is the code of the crawler part of the project TwiNL (2012-2013).
This project also produced code for an 
[interactive website](https://github.com/twinl/website).

The contact person for this project is [Erik Tjong Kim Sang](https://ifarm.nl/).

## Usage instructions

1. download or clone this directory (`crawler`)
2. enter the new directory `crawler` on your system
3. create a new directory `keys` in this directory
4. create four files `makeoauth_NAME_keys.pm` in this directory, where `NAME` is one of `dialect`, `follow`, `locations` and `track`
5. store the Twitter keys of four Twitter accounts in these files; the file `bin/makeoauth.dialect` in this collection contains more information on how to acquire the keys (lines 13-24)
6. start the four crawlers with bin/startall

The crawling software needs valid Twitter credentials, which are
not included here. You will need to store these in files in the
directory keys. Here is an example of one of these files:

```perl
package makeoauth_NAME_keys;

our $consumer_key = "...";
our $consumer_secret = "...";
our $token = "...";
our $oauth_token_secret = "...";
```

Replace the three dots ... by the access keys. 

You do not need to run all the four crawlers. You can also 
choose to run only one of them. In that case comment away 
or remove the redundant lines in the file `bin/startall`.

The search queries of the four crawlers can be found in the 
directory `etc`, in the files `dialect`, `follow`, `locations` 
and `track`.
