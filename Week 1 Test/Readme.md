# Self-Learning Python Tutorial

This script create a json file from given txt file. It extract the emails fron txt file and find their Occurance and EmailType.

### To find Email fromn text file, it use regex.

- \w for word character,digit,underscore
- '+' for one or more word character,digit,underscore, period, dash
- '\.' for '.'(dot) symbol (generally used to separate domain name from the top level domain ) and first_name(.)second_name(@)domain_name(.)top_level_domain
- '-' for dash symbol (used to separate the first name from the last name)

### To find EmailType it use simple logic i.e

- If characters before '@' is seperated by (.) or length of characters before '@' is greater than 7 then **Human**
- Else **Non-Human**
