var joystick = nipplejs.create({
    zone: document.getElementById('static'),
    mode: 'static',
    position: {left: '50%', top: '50%'},
    color: 'red'
});

function send_coordinates(event, data) {
    console.log(event)
    console.log(data)
}

joystick.on('move', send_coordinates)

