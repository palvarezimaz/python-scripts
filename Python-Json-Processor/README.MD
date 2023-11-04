# JQ Clone

A Crickett coding challenge #34
Link: https://codingchallenges.fyi/challenges/challenge-jq/[https://codingchallenges.fyi/challenges/challenge-jq/]
STATUS: Unfinished

# Why?

I haven't scripted in Python for a while and this seemed to be a good opportunity for a quick exercise

## Usage

curl -s <url> | python3 ccjq.py <optional args>

## Optional Arguments
".": prints all
    ie: curl -s -N 'https://dummyjson.com/quotes?limit=2' | python3 ccjq.py "."
"[<n>]": n = number of element of an array
    ie: curl -s 'https://api.github.com/repos/CodingChallegesFYI/SharedSolutions/commits?per_page=3' | python3 ccjq.py "[3]"
"<string>": curl -s -N 'https://dummyjson.com/quotes?limit=2' | python3 ccjq.py "quotes"


# Next steps
- Finish step 3
    a. Support different arg inputs
    b. Support nested args
- Improve the flow of the script
- Do step 4 and 5