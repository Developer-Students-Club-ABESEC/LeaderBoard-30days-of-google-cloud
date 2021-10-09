console.clear();

function getData() {
    var xh = new XMLHttpRequest();
    xh.open(
        "GET",
        "my.json",
        true
    );
    xh.setRequestHeader("Content-Type", "application/json");
    xh.send();
    xh.onload = function () {
        if (this.status == 200) {
            var data = JSON.parse(this.responseText);
            console.log(data);

            var i = 1;
            data.forEach(member => {
                let newRow = document.createElement('div');
                if (member.qcomplete_no ===12){

                
                newRow.innerHTML = `
                <div class="card-container">
                <span class="pro">PRO</span>

                <img src="https://img.icons8.com/ios/100/000000/user-male-circle.png"/>
                    <h3>Rank #${i}</h3>
                    <p><h3><a href="${member.profile_url}" style="color:white;" ><strong>${member.name}</strong></a></h3></p>
                    
                    <div class="skills">
                        <h6>Latest Badges</h6>
                        <ul>
                            <li>${member.badge_count}</li>
                            
                        </ul>
                        <h6>Old Badges</h6>
                        <ul>
                            <li>${member.old_badge_count}</li>
                            
                        </ul>
                    </div>
                    
                </div>
                <br>
                `;
                }
                else{

                newRow.innerHTML = `
                <div class="card-container">

                <img src="https://img.icons8.com/ios/100/000000/user-male-circle.png"/>
                    <h3>Rank #${i}</h3>
                    <p><h3><a href="${member.profile_url}" style="color:white;"  ><strong>${member.name}</strong></a></h3></p>
                   
                    
                    <div class="skills">
                        <h6>Latest Badges</h6>
                        <ul>
                            <li>${member.badge_count}</li>
                            
                        </ul>
                        <h6>Old Badges</h6>
                        <ul>
                            <li>${member.old_badge_count}</li>
                            
                        </ul>
                    </div>
                    
                </div>
                <br>
                `;
                }
              
                i++;
                list.appendChild(newRow);
            });




        } else {
            console.log("Something went wrong.")
        }
    };
}
