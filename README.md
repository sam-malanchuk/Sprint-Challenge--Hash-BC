# Sprint Challenge: Hash Tables and Blockchain

This challenge allows you to practice the concepts and techniques learned over the past week and apply them in a concrete project. This Sprint, we learned how hash tables combine two data structures to get the best of both worlds and were introduced into the fascinating world of blockchains. In your challenge this week, you will demonstrate proficiency by solving algorithms in Python using hash tables and add another key feature to your blockchain.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your work reflects your proficiency in Python and your command of the concepts and techniques in related to hash tables and blockchains.

You have three hours to complete this challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons and your project manager.

## Description

This sprint challenge is divided up into three parts:  Hash tables coding, blockchain coding, and a short interview covering parts of hash tables and blockchain.

## Interview Questions

Explain in detail the workings of a dynamic array:
#### * What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?

To get a new value into a dynamic array from the front you have to check to see that there is space in the back and move the whole array over one causing a O(n) operation. When you need to add a value in the back you can just add it if there is room with a simple O(1) operation as you have the length and know exactly where to place it. If you know the index of the value you need you can retrieve it with an O(1) operation. Removing a value from the array will cause the following values to be moved up. Assuming that an average of the middle of the array then this would result in an O(log n) operation and worst case O(n).

#### * What is the worse case scenario if you try to extend the storage size of a dynamic array?

When the memory array needs to be resized this causes for a new slot in memory to be reserved for it and all the values copied over, resulting in a O(n) operation.

#### Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?

A blockchain is a single linked list of blocks. Each block contains information about itself like a timestamp to records when the block was created, index to keep count of the block's position in the blockchain, transactions to keep track of coins sent from users during this time, proof to generate the blocks secure and difficult to fake hash, and the hash of the previous block.

#### Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?

The blockchain proof of work allows miners to use thier processing power over a long period of time for a set proof difficulty looking for the proof. The proof does not have a simple calculation that can figure it out so it must be a guess and check algorithm. One the miner client finds a suitable proof meeting the blockchain guidelines it shows the chain, if the chain find the proof to work it hashes the block with the proof moving on to the next block. The hash of the block is placed in the body of the next block causing an unbreakable chain. An attacker might try to fake a proof or hash to change some contents of a block but they would have to go back and change the hash of the block after it too. If they are working on the newest block in the chain they would require at least 50% of all the current mining power to beat the others to getting the proof and providing false information. 
 
## Project Set Up

#### [Hash Tables]

For the hash tables portion of the sprint challenge, you'll be working through two algorithm problems that are amenable to being solved efficiently using a hash table. You know the drill at this point. Navigate into each exercise's directory, read the instructions for the exercise laid out in the README, implement your solution in the .py skeleton file, then make sure your code passes the tests by running the test script with make tests.

A hash table implementation has been included for you already. Your task is to get the tests passing (using a hash table to do it). You can remind yourself of what hash table functions are available by looking at the hashtable.py file that is included in each exercise directory (note that the hash table implementations for both exercises differ slightly).

*You may not use any advanced, built-in Python functions to solve these problems.*

#### [Blockchain]

For the blockchain portion of the challenge, you will be writing code for a new miner that will solve a different Proof of Work algorithm than the one we have been working with.

Your goal is to mine at least 16 coins.  Keep in mind that with many people competing over the same coins, this may take a long time.  By our math, we expect that an average solution should be the first to find a solution at least 20 times in an hour or two of mining.  

## Minimum Viable Product

#### [Hash Tables](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/hashtables)

#### [Blockchain](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/blockchain)


### Rubric

| *OBJECTIVE*                                                                                                     | *TASK*             | *1 - DOES NOT MEET EXPECTATIONS*                                                                                            | *2 - MEETS EXPECTATIONS*                                                                                                       | *3 - EXCEEDS EXPECTATIONS                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| implement and describe how high-level array functions work down to the memory level                             | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
| implement and utilize basic hash table + handle collisions and resizing in a hash table                         | Hash Problem 1 & 2 | Tests do not pass on one or both problems, or solutions do not use hash tables.                                             | Tests pass on both problems.  Solution utilizes a hash table.                                                                  | Tests pass on on both problems with solutions utilizing hash tables, linear runtime complexity, no flake8 complaints.                                 |
| diagram and code a simple blockchain, utilizing a cryptographic hash                                            | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
| utilize a Proof of Work process to protect a blockchain from attack                                             | Blockchain Problem | The student is unable to mine at least 16 coins before the end of lunch.                                                               | The student was able to mine at least 16 coins before the end of lunch.                                                                   | The student presented a unique solution that was able to mine more than 1000 coins before the end of lunch.                                            |
| build a protocol to allow nodes in a blockchain network to communicate to share blocks and determine consensus. | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |

## Grading
The grade for this sprint challenge is the average of the number of points received (points/15)
