def transform(legacy_data):
    new_mapping = dict()
    for points,letters in legacy_data.items():
      new_mapping.update({letter.lower() : points for letter in letters})  
    return new_mapping
        
