def get_mention(message):
    for entity in message.entities:
        if entity.type == 'mention':
            start_position = message.text.find('@')
            mention = message.text[start_position:start_position + entity.length]
            return mention
    return None
