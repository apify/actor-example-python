from apify import Actor


async def main():
    async with Actor:
        # Get the value of the actor input
        actor_input = await Actor.get_input() or {}

        # Structure of input is defined in .actor/input_schema.json
        first_number = actor_input.get('first_number')
        second_number = actor_input.get('second_number')

        print(f'First number: {first_number}')
        print(f'Second number: {second_number}')

        result = first_number + second_number

        print(f'The result is: {result}')

        # Structure of output is defined in .actor/actor.json
        await Actor.push_data([
            {
                'first_number': first_number,
                'second_number': second_number,
                'sum': result,
            },
        ])
