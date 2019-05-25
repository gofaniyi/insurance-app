from api.models.attribute import Attribute


class TestAttributeModel:

    def test_save(self, init_db, new_risk_type):
        """Test for creating a new attribute
        
            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_risk_type (RiskType): Fixture to create a new risk type
        """
        attribute = Attribute(
            _key='serial_number',
            label='serial_number',
            is_required=False,
            input_control='text',
            choices=None)
        new_risk_type.attributes.append(attribute)
        new_risk_type.save()
        assert attribute == attribute.save()


    def test_update(self, new_risk_type_with_attribute):
        """Test for update method
        
            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_risk_type_with_attribute (RiskType): Fixture to create a new risk type
        """
        new_risk_type_with_attribute.attributes[0].update(label='color', choices='red,brown', input_control='radio button')
        assert new_risk_type_with_attribute.attributes[0].label == 'color'
        assert new_risk_type_with_attribute.attributes[0].label == 'color'
        assert new_risk_type_with_attribute.attributes[0].choices == 'red,brown'

    def test_get(self, init_db, new_attribute):
        """Test for get method
        
            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_attribute (RiskType): Fixture to create a new risk type
        """
        assert Attribute.get(new_attribute.id) == new_attribute


    def test_attribute_model_string_representation(self, init_db, new_attribute):
        """ Should compute the string representation of an attribute
        
        Args:
            init_db(SQLAlchemy): fixture to initialize the test database
            new_attribute (object): Fixture to create a new attribute
        """
        assert repr(new_attribute) == f'<Attribute {new_attribute.label}>'
