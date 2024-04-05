
from models.queries import get_data_user


from lexicon.lexicon import LEXICON_DATABASE

def show_plan(id_user: int, day: str) -> str:
    """Function will greet the user and show his plan for chose day."""
    plan = get_data_user(id_user, LEXICON_DATABASE[day])
    if plan is None:
        plan = ("Function returned None value",)

    return f"""
Hey👋, here's your plan for <b>{day}</b>:

{plan[0]}
"""




# res = show_plan(1201, "Monday")
# print(res)

# res2 = show_plan(1201, "Sunday")
# print(res2)

# res3 = show_plan(1201, "Monday")
# print(res3)
