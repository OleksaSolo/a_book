from Bot import *

from class_console_output import (
    FactoryOutput,
    Terminals,
    TerminalOutput,
    TelegramOutput,
    ViberOutput,
)

def when_out(pre_init: object = None) -> None:
    factory_output = FactoryOutput()
    factory_output.register_output(TerminalOutput)
    factory_output.register_output(TelegramOutput)
    factory_output.register_output(ViberOutput)
    args = factory_output.get_registered_services()
    # print(f"args: {args}")

    output_terminal = Terminals(args[0])

    print(f"output_terminal: {output_terminal}")
    output_kwargs = {}
    if output_terminal == Terminals.TELEGRAM:
        output_kwargs = {
            "token": "88734823842346ge8934637687646746328-90903222121ab22e"
        }
    elif output_terminal == Terminals.VIBER:
        output_kwargs = {"token": "632676746-89437487804-48497434648364-4348948934"}

    output_terminal=factory_output.create_output(output_terminal, **output_kwargs)


if __name__ == "__main__":
    when_out()
    print('Hello. I am your contact-assistant. What should I do with your contacts?')
    bot = Bot()
    bot.book.load("auto_save")
    commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    while True:
        action = input('Type help for list of commands or enter your command\n').strip().lower()
        if action == 'help':
            format_str = str('{:%s%d}' % ('^',20))
            for command in commands:
                print(format_str.format(command))
            action = input().strip().lower()
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        else:
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        if action == 'exit':
            break
