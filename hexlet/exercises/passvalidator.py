import copy


class PasswordValidator():
    OPTIONS = {
        'min_len': 8,
        'contain_numbers': False,
        }
    # BEGIN (write your solution here)

    new_options = {}

    def __init__(self, **kwargs):
        self.new_options = copy.deepcopy(self.OPTIONS)
        print('OPTIONS =', self.new_options)
        for key in self.new_options.keys():
            if key in kwargs:
                self.new_options[key] = kwargs[key]
        print('new opt: ', self.new_options)

    def validate(self, password):
        errors = {}
        if not self.minlen(password):
            errors['min_len'] = 'too small'
        if self.new_options['contain_numbers'] is True:
            if not self._has_number(password):
                errors['contain_numbers'] = 'should contain at least one number'
        return errors

    def minlen(self, password):
        return len(password) >= self.new_options['min_len']
    # END

    def _has_number(self, password):
        return any(char.isdigit() for char in password)


def test_validate_with_default_options():
    validator = PasswordValidator()
    errors1 = validator.validate('qwertyui')
    print('default 1', not errors1)

    errors2 = validator.validate('qwerty')
    print('default 2',  errors2 == {'min_len': 'too small'})

    errors3 = validator.validate('another-password')
    print('default 3', not errors3)


def test_validate_with_options():
    options = {'contain_numbers': True}
    validator = PasswordValidator(**options)
    errors1 = validator.validate('qwertya3sdf')
    print('with options 1', not errors1)

    errors2 = validator.validate('qwerty')
    print('with options 2', errors2 == {
        'min_len': 'too small',
        'contain_numbers': 'should contain at least one number'
        })
    errors3 = validator.validate('q23ty')
    print('with options 3', errors3 == {'min_len': 'too small'})


def test_validate_with_incorrect_options():
    validator = PasswordValidator(contain_numberz=None)
    errors1 = validator.validate('qwertya3sdf')
    print('with incorrect 1', not errors1)

    errors2 = validator.validate('qwerty')
    print('with incorrect 2', errors2 == {'min_len': 'too small'})


if __name__ == '__main__':
    # test_validate_with_default_options()
    test_validate_with_options()
    test_validate_with_incorrect_options()
