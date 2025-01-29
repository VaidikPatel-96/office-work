document.addEventListener("DOMContentLoaded", function() {
    const dateElement = document.getElementById("date");
    const dayElement = document.getElementById("day");
    const monthElement = document.getElementById("month");
    const yearElement = document.getElementById("year");

    function updateCalendar() {
        const today = new Date();
        const date = today.getDate();
        const day = today.toLocaleString('default', { weekday: 'long' });
        const month = today.toLocaleString('default', { month: 'long' });
        const year = today.getFullYear();

        dateElement.textContent = date;
        dayElement.textContent = day;
        monthElement.textContent = month;
        yearElement.textContent = year;
    }

    updateCalendar();
});