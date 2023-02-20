// get the current date and time
var currentDate = new Date();

// set the current month and year
var currentMonth = currentDate.getMonth();
var currentYear = currentDate.getFullYear();

// add event listeners to previous and next month buttons
document.getElementById("prev-month").addEventListener("click", showPrevMonth);
document.getElementById("next-month").addEventListener("click", showNextMonth);

// function to generate the monthly calendar for a given month and year
function generateCalendar(month, year) {
  // get the element where the calendar will be displayed
  var calendar = document.getElementById("calendar");

  // clear the calendar
  calendar.innerHTML = "";

  // create the header with the month and year
  var header = document.createElement("h2");
  header.textContent = new Date(year, month).toLocaleString("default", { month: "long" }) + " " + year;
  calendar.appendChild(header);

  // create the table element
  var table = document.createElement("table");

  // create the header row with day names
  var headerRow = document.createElement("tr");
  var daysOfWeek = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
  for (var i = 0; i < daysOfWeek.length; i++) {
    var th = document.createElement("th");
    th.textContent = daysOfWeek[i];
    headerRow.appendChild(th);
  }
  table.appendChild(headerRow);

  // get the number of days in the month
  var numDays = new Date(year, month + 1, 0).getDate();

  // get the day of the week for the first day of the month
  var firstDayOfMonth = new Date(year, month, 1).getDay();

  // create the calendar cells
  var day = 1;
  for (var i = 0; i < 6; i++) {
    var row = document.createElement("tr");
    for (var j = 0; j < 7; j++) {
      var cell = document.createElement("td");
      if (i === 0 && j < firstDayOfMonth) {
        // leave the cell empty before the first day of the month
      } else if (day > numDays) {
        // leave the cell empty after the last day of the month
      } else {
        // add the day number to the cell
        cell.textContent = day;
        day++;
      }
      row.appendChild(cell);
    }
    table.appendChild(row);
  }

  // add the table to the calendar
  calendar.appendChild(table);
}

// function to show the previous month
function showPrevMonth() {
  currentMonth--;
  if (currentMonth < 0) {
    currentMonth = 11;
    currentYear--;
  }
  generateCalendar(currentMonth, currentYear);
}

// function to show the next month
function showNextMonth() {
  currentMonth++;
  if (currentMonth > 11) {
    currentMonth = 0;
    currentYear++;
  }
  generateCalendar(currentMonth, currentYear);
}

// generate the calendar for the current month and year
generateCalendar(currentMonth, currentYear);