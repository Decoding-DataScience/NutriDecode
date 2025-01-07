from dataclasses import dataclass
from typing import Dict, List

@dataclass
class FoodLabel:
    nutritional_info: Dict[str, str]
    ingredients: List[str]
    allergens: List[str]
    eco_impact: Dict[str, str]

    def to_dict(self) -> Dict:
        return {
            'nutritional_info': self.nutritional_info,
            'ingredients': self.ingredients,
            'allergens': self.allergens,
            'eco_impact': self.eco_impact
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'FoodLabel':
        return cls(
            nutritional_info=data['nutritional_info'],
            ingredients=data['ingredients'],
            allergens=data['allergens'],
            eco_impact=data['eco_impact']
        ) 