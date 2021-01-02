## CAP Theorem
    
Distributed database system has to make a tradeoff between consistency and availability

Pick 2 out of these 3: only 2 of the 3 are possible at the same time: 
- Consistency - Cohérence
    tous les nœuds du système voient exactement les mêmes données au même moment
    User retrieves the same information no matter wich node he connect to
    Important for: finance (accounts) 
- Availability
    garantie que toutes les requêtes reçoivent une réponse. 
    Every user is able to get the data
    Response of the system even if its a "unsuccessful" operation
    Important when need to access a data at all times (whatsapp status when offline...)
- Partition Tolerance
    aucune panne moins importante qu'une coupure totale du réseau ne doit empêcher le système de répondre correctement (ou encore : en cas de morcellement en sous-réseaux, chacun doit pouvoir fonctionner de manière autonome).
    Partition = communication break between nodes (network failure, server crash)
    The system should still be able to work even if there is a partition meaning that if a node fails to communicate, then one of the replicas of the nodes should be able to retrieve the data