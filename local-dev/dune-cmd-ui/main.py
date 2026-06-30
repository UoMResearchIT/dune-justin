from dashboard.fields.fieldset import FieldSet
from dashboard.form.command_form import CommandForm
from dashboard.fields.select import Select
from dashboard.fields.date_selector import DateSelector
from dashboard.fields.text_field import TextField
from dashboard.fields.checkbox import Checkbox
from dashboard.fields.radio import RadioGroup, Radio


def output_html(
    content: str,
    template_html_fp: str = "template.html",
    output_html_fp: str = "index.html",
):
    with open(template_html_fp, "r") as f:
        template = f.read()
        html = template.format(content=content)

    with open(output_html_fp, "w") as f:
        f.write(html)
    print(f"[OK] output at ./{output_html_fp}")


def main():
    form = CommandForm(
        fields=[
            FieldSet(
                name="My FieldSet",
                fields=[
                    Select(
                        name="select1",
                        label_name="Select1",
                        options=["1", "2", "3"],
                        value="2",
                        
                    ),
                    Select(
                        name="select2",
                        label_name="Select2",
                        options=["A", "B", "C"],
                        value="B",
                        
                    ),
                    DateSelector(name="date1", label_name="Date1"),
                    TextField(
                        name="text1",
                        label_name="TEXT_FIELD",
                        id="my_text1",
                        placeholder=" 5 <= x <= 10",
                        validators=["required number min:5 max:10"],
                        
                    ),
                    RadioGroup(
                        name="radio1",
                        options=[
                            {"value": "html", "label": "HTML", "id": "html"},
                            {"value": "javascript", "label": "JavaScript", "id": "javascript"},
                            {"value": "css", "label": "CSS", "id": "css"},
                        ],
                        value="css",
                    ),
                    Radio(
                        name="radio2",
                        value="python",
                        label_name="Python",
                        id="python",
                        checked=True,
                    ),
                    Checkbox(
                        name="checkbox1",
                        label_name="CHECKBOX1",
                        id="my_checkbox1",
                        validators=["required"],
                        value="asdfasdf",
                        is_checked=True,
                    ),
                    Checkbox(
                        name="checkbox2",
                        label_name="CHECKBOX2",
                        id="my_checkbox2",
                        validators=["required"],
                        value="123456",
                    ),
                    TextField(
                        name="text2",
                        label_name="TEXT_FIELD_2",
                        id="my_text2",
                        conditional_display=["my_checkbox2:checked"],                        
                    ),
                    Select(
                        name="select3",
                        label_name="Select3",
                        options=["X", "Y", "Z"],
                        value="Y",
                        conditional_display=["my_checkbox2:checked"],
                    ),
                    Radio(
                        name="radio3",
                        value="apple",
                        label_name="Apple",
                        id="apple",
                        conditional_display=["my_checkbox2:checked"],
                    ),
                    RadioGroup(
                        name="radio4",
                        options=[
                            {"value": "bus", "label": "Bus", "id": "bus"},
                            {"value": "taxi", "label": "Taxi", "id": "taxi"},
                            {"value": "van", "label": "Van", "id": "van"},
                        ],
                        conditional_display=["my_checkbox2:checked"],
                    ),
                    DateSelector(name="date2", label_name="Date2", conditional_display=["my_checkbox2:checked"]),
                    Checkbox(
                        name="checkbox3",
                        label_name="CHECKBOX3",
                        id="my_checkbox3",
                        validators=["required"],
                        value="abcd",
                        conditional_display=["my_checkbox2:checked"],
                    ),
                ],
            )
        ],
        cgi_method="filter_data",
    )

    form_html = form.render()
    
    output_html(
        form_html, template_html_fp="index_template.html", output_html_fp="index.html"
    )


main()
