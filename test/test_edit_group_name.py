from random import randrange


def test_edit_group_name(app):
    old_list = app.groups.get_group_list()

    index = randrange(len(old_list))

    app.groups.edit_group_name(index, "changed_group_XX")
    new_list = app.groups.get_group_list()

    old_list[index] = "changed_group_XX"

    assert sorted(old_list) == sorted(new_list)
