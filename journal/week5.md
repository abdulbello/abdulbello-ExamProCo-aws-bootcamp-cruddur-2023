# Week 5 — DynamoDB and Serverless Caching

So we are in week five and its Dynamo DB time.

I've just finished watching the recording of the livestream between Andrew and Kirk, and my initial reactions are that "okay, that was a lot, i need to stop and just try to recollect all i've learnt". Just like with the RDS week where i had to go learn about data normalization and stuff about RDS, for Dynamo DB i had to keep pausing the recording to go read about No SQL and Dynamo DB specifically from the Amazon documentation. I might not have understood half of what i was able to grab without doing the inbetween reading.

I like Dynamo DB, it just seems like data modelling your DB is a very subjective process and two different people could come up with different models and would not necessarily be wrong. During the stream i learnt that its better you identify your data access patterns and let those guide your decision making during the modelling thought process.

During the modelling session, i am struggling to understand why we have to create two different message groups per conversation(one from the user and the other_user perspective). It just feels redundant, even though Kirk did say, its okay to repeat data in No SQL design, as long as it makes sense and helps you avoid extra compute caused by querying. I'm thinking we could query a message group UUID and display information based on the context of logged in user. (I might be wrong).


I was able to watch Ashish's video on securing Dynamo DB and it had alot of similarities with securing RDS (because they are DBs). Some interesting new stuff i learnt is that you can create a DAX cluster in your vpc, give it read only or read/write permissions to secure and improve performance of your dynamo db table. I also learnt that each region has an endpoint url format for dynamo db, not sure if it applies to all services tho.


Finally, i was able to completly implement messaging in the cruddur app backed by dynamo db. We also created a lambda function to update the last message in a message group when the user is in the message group view. It took a while to get the permissions sorted due to some weird errors, but i eventually got it working.

I would like to be part of another ddb modelling session to cement the knowledge. But so far so good.

I look forward to the next week's work.









