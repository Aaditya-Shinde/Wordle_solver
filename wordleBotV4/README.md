The approach to V4 is to eliminate as many possible answers as we can. 
To do this, we can first see that the method used to eliminate answers is more sophisticated. If the feedback we get from the user is not the same as when we compare the guess to each answer, it cannot be the hidden_word.
Now we see that there are only 5^5 possible feedbacks for any given guess. If we take each guess and then consider each possible answer, we can group the answers based on the feedback recieved.
We should imagine the worst case senario, and in that case, the biggest of these groups will be left over. Therefore, we try to minimize the biggest group.
For the GUI, just click the buttons until the colors match what you see on wordle
