from dashboard.fields.fieldset import FieldSet
from dashboard.form.command_form import CommandForm
from dashboard.fields.select import Select
from dashboard.fields.date_selector import DateSelector
from dashboard.fields.text_field import TextField
from dashboard.fields.checkbox import Checkbox


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
                name="Basic",
                fields=[
                    TextField(
                        name="description",
                        label_name="description",
                        id="description",
                        placeholder="workflow description",
                        validators=["required"],
                        
                    ),
                    TextField(
                        name="scope",
                        label_name="scope",
                        id="scope",
                        placeholder="workflow scope",
                        validators=["required alphanum"],
                    ),
                ],
            ),
            FieldSet(
                name="Input source",
                fields=[
                    Select(
                        name="mode",
                        label_name="Mode",
                        options=["--mql QUERY", "--monte-carlo COUNT", "none"],
                        default_value="none",
                    ),
                ],
            ),
            FieldSet(
                name="Refind (MQL Resubmission)",
                fields=[
                    TextField(
                        name="refind-interval-hours",
                        label_name="--refind-interval-hours",
                        id="refind-interval-hours",
                        placeholder="Refind interval (hours)",
                        validators=["required number min:1 max:100"],
                    ),
                    DateSelector(
                        name="refind-end-date",
                        label_name="--refind-end-date",
                        # validators=["required date"],
                    ),
                ]
            ),
            FieldSet(
                name="Campaign and output",
                fields=[
                    TextField(
                        name="campaign-id",
                        label_name="--campaign-id",
                        id="campaign-id",
                        placeholder="campaign-id",
                        validators=["alphanum"],
                    ),
                    TextField(
                        name="workflow-id-file",
                        label_name="--workflow-id-file",
                        id="workflow-id-file",
                        placeholder="workflow-id-file",
                        validators=["alphanum"],
                    ),
                ]
            )
        ],
        cgi_method="filter_data",
    )

    form_html = form.render()
    
    output_html(
        form_html, template_html_fp="index_template.html", output_html_fp="index.html"
    )


main()
