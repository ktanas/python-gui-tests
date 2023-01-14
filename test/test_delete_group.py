from random import randrange


def test_delete_group(app):
    old_list = app.groups.get_group_list()
    if len(old_list) == 0:
        app.groups.add_new_group("A")
        old_list.append("A")

    index = randrange(len(old_list))

    app.groups.delete_group(index)

    new_list = app.groups.get_group_list()

    assert len(new_list) == len(old_list) - 1
    old_list[index:index+1] = []
    assert old_list == new_list
