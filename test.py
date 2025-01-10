def process_tickets(tickets):
    priority_queue = {}
    for ticket in tickets:
        ticket_id, ticket_priority = ticket.split(":")
        #priority = int(priority)
        if priority in priority_queue:
            priority_queue[priority].append(ticket_id)
        else:
            priority_queue[priority] = [ticket_id]

    priorities = sorted(priority_queue.keys(), reverse=True)
    processed_tickets = []
    for priority in priorities:
        processed_tickets.extend(priority_queue[priority])
    return processed_tickets  

print(process_tickets(['T123:4', 'T124:1', 'T125:3', 'T126:5', 'T127:3']))