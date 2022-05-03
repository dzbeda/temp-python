# Coding Assignments - Session 2 


* [people.json](../session2/src/resources/people.json) is a file that contains names of people along with their ages
* [age_ranges.json](../session2/src/resources/age_ranges.json) is file that contains a list of people age ranges

Implement the [assignment1.py](src/assignment1.py) script and its function `run(people_file_path, age_range_file_path)` So that the script will be able to perform the following:

1. Accept the two json file path as command line arguments (See [CMD run](#command-line-run) below)
1. Accept an environment variable called `YAML_OUTPUT_PATH` (See [CMD run](#command-line-run) below)
1. Create a folder (if not exists) based on the given input of `YAML_OUTPUT_PATH`
1. Parse the two .json files into a yaml file:
  * located within the given path in `YAML_OUTPUT_PATH`
  * File name must be `people_by_age_range.yaml`
  * A [specific logic](#parsing-logic) must be performed before saving the `yaml` file.

## Parsing Logic

The purpose of the script logic is to create people groups based on the given age ranges. Each person is placed in a group based on his given age in 
[people.json](../session2/src/resources/people.json) and the created age group based on the age ranges provided in
[age_ranges.json](../session2/src/resources/age_ranges.json).

### People
Each person has a name and age represented in the json file.

Within the output yaml file:
 * A person should only be displayed with his name as key and age as value (e.g. `George: 56`).
 * A person will belong to an age group if is his age is equal to or bigger than the smaller number in each age range (e.g. a 10 year old will not be in a group of 0-10 but will be in a group of 10-20)

### Age Ranges
Each age range is represented in the output yaml file as a key to the people group. The key is a string that represents the small range to the bigger range (e.g. `0 - 10`)

The age range will be created based on the following logic:

* First range always starts from 0 regardless of the given age ranges
* If a person's age exceeds the given age range, a new range will be created based on ** the oldest person age in the given people data + 1 year** (the added +1 year is needed in order for the person to be counted within this group) 

#### Working Example

For a given people data of 5 people:
    George which is aged 40
    Michelle which is aged 30
    Judy which is aged 20
    Aaron which is aged 10
    
And for a given list of age ranges [20,30]

The output `people_by_age_range.yaml` file should look as follows:

```yaml
---
0 - 20:
  Aaron: 10
20 - 30:
  Judy: 20 
30 - 41:
  Michelle: 30
  George: 40
```    

> ⚠️ Notice the following:
>1. 0 was added and also created the first age range (0-20) 
>1. Judy which is aged 20  (equals to one of the given ranges [20,30]) belongs to the (20-30) age range
> and NOT the (0 - 20) age range.
>1. George who is aged 40 created a new age range (30-41) 
>1. Age ranges are sorted by age (youngest to oldest)
>1. People inside an age range are also sorted by age (Michelle(30) is first since she is younger than George(40))


## Command Line Run 
The [assignment1.py](src/assignment1.py) script should be called from the command line along with the file path and environment variable as follows:

```sh
# This example assumes you run this command from the root folder of the repo. If not adjust as you need
$ YAML_OUTPUT_PATH="some-path/to-some-folder" python assignments/session2/src/assignment1.py assignments/session2/src/resources/people.json assignments/session2/src/resources/age_ranges.json
```

**Happy coding!** \
![coding!](https://media.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif)
