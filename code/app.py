import shiny
from shiny import App, ui, render, reactive
import pandas

# UI
app_ui = ui.page_fluid(
    ui.h2("Male Body Fat Calculator"),
    
    # Units select
    ui.input_radio_buttons(
        "unit", 
        "Choose Unit System:", 
        {"metric": "Metric (cm)", "us": "US (inches)"}
    ),
    
    # Input Features
    ui.input_numeric("abdomen", "Abdomen (cm/inches):", 75.0),
    ui.input_numeric("wrist", "Wrist (cm/inches):", 16.5),
    ui.input_numeric("height", "Height (cm/inches):", 178.0),
    
    # Show Body Fat Formula
    ui.output_text_verbatim("formula"),
    
    # Show Calculated Body Fat
    ui.output_text_verbatim("body_fat"),
    
    # The American Council on Exercise Body Fat Categorization
    ui.h4("The American Council on Exercise Body Fat Categorization"),
    ui.output_table("ace_table"),
    
    # Jackson & Pollock Ideal Body Fat Percentages
    ui.h4("Jackson & Pollock Ideal Body Fat Percentages"),
    ui.output_table("jackson_pollock_table"),

    # Contact
    ui.h4("Github"),
    ui.output_text("github")
)

# Server
def server(input, output, session):
    
    # Body Fat Formula
    @reactive.Calc
    def body_fat_percentage():
        unit = input.unit()
        abdomen = input.abdomen()
        wrist = input.wrist()
        height = input.height()
        
        if unit == "metric":
            # Metric Units
            body_fat = 9.42844127683235 + 32.97367213*(abdomen-69.4)/(118-69.4) - 6.5546632*(wrist-16.1)/(20.4-16.1) - 5.1692971*(height/2.54-64)/(77.75-64)
            formula = "Body Fat = 9.42844127683235 + 32.97367213*(abdomen-69.4)/(118-69.4) - 6.5546632*(wrist-16.1)/(20.4-16.1) - 5.1692971*(height/2.54-64)/(77.75-64)"
        else:
            # US Units
            body_fat = 9.42844127683235 + 32.97367213*(abdomen*2.54-69.4)/(118-69.4) - 6.5546632*(wrist*2.54-16.1)/(20.4-16.1) - 5.1692971*(height-64)/(77.75-64)
            formula = "Body Fat = 9.42844127683235 + 32.97367213*(abdomen*2.54-69.4)/(118-69.4) - 6.5546632*(wrist*2.54-16.1)/(20.4-16.1) - 5.1692971*(height-64)/(77.75-64)"
        
        return body_fat, formula
    
    # Show Body Fat Formula
    @output
    @render.text
    def formula():
        return body_fat_percentage()[1]
    
    # Show Calculated Body Fat
    @output
    @render.text
    def body_fat():
        return f"Calculated Body Fat: {body_fat_percentage()[0]:.2f}%"
    
    # The American Council on Exercise Body Fat Categorization
    @output
    @render.table
    def ace_table():
        return pandas.DataFrame({
            "Category": ["Essential Fat", "Athletes", "Fitness", "Average", "Obese"],
            "Men (%)": ["2-5", "6-13", "14-17", "18-24", "25+"]
        })
    
    # Jackson & Pollock Ideal Body Fat Percentages
    @output
    @render.table
    def jackson_pollock_table():
        return pandas.DataFrame({
            "Age Group": ["20-29", "30-39", "40-49", "50-59", "60+"],
            "Men Ideal BF (%)": [8.5, 11.5, 14.5, 17.5, 20.3]
        })

    # Contact
    @output
    @render.text
    def github():
        return "Feel free to contact us: https://github.com/unimodular/Bodyfat-Prediction.git"

# Run App
app = App(app_ui, server)

