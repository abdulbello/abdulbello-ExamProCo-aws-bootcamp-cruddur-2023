# Week 3 — Decentralized Authentication

Hello!!!

Finally got a chance to catch up on the bootcamp.. I'm about two weeks behind schedule as i had to work on my Master's thesis concurrently.


Anyway, i've created my cognito user pool and looking forward to using it.. I have always wondered how it works especially when i was preparing for the AWS SOlutions Architect certification.

We configured the user pool without setting it to generate a client app secret. I wonder if thats good security. We'll see.


During the Cognito custom pages exercise, i made some changes outside Andrew's instructions. I allowed users to either login with email/username (i think it gives more flexibility). All i had to do was pass username as username in the signup page mappings. I also changed the label on the confirmation page to say the user can verify their email by providing username/email info. I don't see this as a security issue since the user still has to provide the code sent to their email.

<img width="1440" alt="image" src="https://user-images.githubusercontent.com/112012120/227217624-81f05113-2c39-4927-aeb6-eed5fadf06d4.png">


As part of the strectch exercises, i need to ensure the user signup confirmation code, resend feature works.


I'm currently watching the video for the cognito jwt server side verifier and it took way more time than i thought. A good knowledge to have is how to architect a software i.e Structure a software to know where to put classes, how to make them communicate and interoperate. I'll find some time to learn this. But yeah, there is a lot of information being learnt here and it really makes me appreciate Andrew and his entire team.

Watching the jwt video helped me get a better idea of how cors work, pre-processing a request, and structuring your application to separate libraries from services.

<img width="1440" alt="image" src="https://user-images.githubusercontent.com/112012120/227585457-1e3ac01e-34f6-474e-b1c3-33fbd6ef1d3c.png">


It was inspiring watching Andrew's recording on other JWT implementation considerations. He inspired me when he spoke about reading the entire rfc documentation proposing JWTs. I've taken some time to read parts of it as well and it has helped me understand how they work as well. I said i'm inspired because i typically do not like to read long stuff, but now i am more open to it for the benefits.

I am about two weeks behind schedule for the bootcamps and have not done any homework challenges for this week. I've read through them and they seem time consuming. I'm wondering if i can just submit my assignment but come back later in the bootcamp to try out some of the homework challenges.





