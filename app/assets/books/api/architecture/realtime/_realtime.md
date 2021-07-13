# REALTIME APP

A Real time application is a reactive application that follows the rythm imposed by its environment
Each output Oi should be produced before the reception on the next input Ii+1

   I⁰        I¹        I²        I³      …
   │         │         │         │
---━━━━--🔸--━━━━--🔸--━━━━--🔸--━━━━-------…
       │        │          │        │
       ↓        ↓          ↓        ↓
       O⁰       O¹         O²       O³      …

🔸    Pause
━━━━  Reaction       


Real-time data refers to anything that creates useful insights that can immediately be processed and deployed, based on data collected as they occur in the real world.   
The result is more efficient, more accurate information that can be used to make informed decisions. It was very important to collect, ingest and analyze the dynamic data coming from various sources in a more near real time manner to target the customers at a specific point of time to achieve better results for this specific use case.

Components of a real-time data source framework:
- Data source enabling CDC (change data capture) / change tracking
- Streaming or messaging brokers
- Data Consumers or Processors


## More
- https://www.sqlservercentral.com/articles/real-time-data-streams-from-sql-server-using-kafka-connect-in-the-cloud