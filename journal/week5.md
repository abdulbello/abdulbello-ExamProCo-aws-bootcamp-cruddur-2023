# Week 5 — DynamoDB and Serverless Caching

So we are in week five and its Dynamo DB time.

I've just finished watching the recording of the livestream between Andrew and Kirk, and my initial reactions are that "okay, that was a lot, i need to stop and just try to recollect all i've learnt". Just like with the RDS week where i had to go learn about data normalization and stuff about RDS, for Dynamo DB i had to keep pausing the recording to go read about No SQL and Dynamo DB specifically from the Amazon documentation. I might not have understood half of what i was able to grab without doing the inbetween reading.

I like Dynamo DB, it just seems like data modelling your DB is a very subjective process and two different people could come up with different models and would not necessarily be wrong. During the stream i learnt that its better you identify your data access patterns and let those guide your decision making during the modelling thought process.

During the modelling session, i am struggling to understand why we have to create two different message groups per conversation(one from the user and the other_user perspective). It just feels redundant, even though Kirk did say, its okay to repeat data in No SQL design, as long as it makes sense and helps you avoid extra compute caused by querying. I'm thinking we could query a message group UUID and display information based on the context of logged in user. (I might be wrong) 









