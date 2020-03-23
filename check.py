# import click
# import argparse

# @click.command()
# @click.option("--project", "-p", default="releai-dev", help="GCP project", prompt='your project')
# @click.option("--bank_name", "-b", help="Name of the client", prompt='your Bank-name')
# @click.option("--version", "-v", default="v1", help="RELE.AI app version", prompt='your version')
# def _run(project, version, bank_name):
#     options = {
#         "project": project,
#         "bank_name": bank_name,
#         "version": version
#     }
#     click.echo(options)
#     return options

# if __name__ == "__main__":
#     options = _run()
    # print("here", options)
# import math
def saar():
    try:
        a = int(input('press nubmer: '))
        b = int(input('press nubmer: '))
        add = a + b
        sub = a - b
        mul = a * b
        _sum = add + add
        print('a + b:', add)
        print('a - b:', sub)
        print('a * b:', mul)
        print('add + add', _sum)
    except:
        print("Please insert only numbers.")
if __name__ == "__main__":
    saar()