
# Spacerep
Spacerep is a small Python CLI, built on fire, tinydb to help busy devs (or anybody with a penchant for terminal) track down their online learning resources in an optimal way.
Specifically it uses the SM2 spaced repetition algorithm to calculate the forgetting curve and therefore the best intervals to fortify the study material based on number of repetitions and ease of recollection.

# History of Spaced Repetition

**Spaced Repetition** is a learning technique that involves increasing intervals of time between subsequent reviews of previously learned material, aiming to exploit the psychological spacing effect. The technique was pioneered by Hermann Ebbinghaus in the late 19th century, and has been refined over the years, with notable contributions from Piotr Wozniak, who developed the SuperMemo series of software. The SuperMemo introduced the **SM2 algorithm** in 1987.

The SM2 algorithm is designed to determine the optimal intervals for review. After each review, if the item is remembered, the interval until the next review is increased. If the item is not remembered, the interval is shortened or reset. The calculation of these intervals considers factors such as the repetition count, the easiness factor, and the length of the previous interval. SM2’s effectiveness is backed by psychological and cognitive science research on the "forgetting curve" and "spacing effect".

The proof of its effectiveness comes from empirical evidence both in academic settings and in personal learning contexts. Wozniak's own mastery of a vast array of topics is often cited as anecdotal proof. Furthermore, scientific studies also support spaced repetition, showing that there is enhanced recall and long-term retention when information is revisited at gradually increasing intervals, a process which is simulated effectively by the SM2 algorithm.

# Proof of Concept
The CLI is still in the POC phase but offers the MVP to those willing to try it
