  function authInfo(response){
      console.log(response)
      VK.Api.call('users.get', {user_ids: response.session.user.id, fields: 'bdate, photo_50', v:'5.73'}, function(user){
          fetch('http://127.0.0.1:5000/user', {
              method: 'POST',
              body: JSON.stringify(user),
              headers: {
                  'Content-Type': 'application/json;charset=utf-8'
              }
          })
          .then(function (user_response) {
              if (user_response.status !== 200) {
                  console.log(user_response.status);
                  return;
              }

              user_response.json().then(function (data){
                  console.log(data)
              })

              VK.Api.call('friends.get', {user_id: response.session.user.id, fields: "bdate, photo_50", v:"5.73"}, function(friends) {
                  user_id = response.session.user.id
                  friends.response.items.push(user_id)
                  fetch('http://127.0.0.1:5000/friends', {
                      method: 'POST',
                      body: JSON.stringify(friends),
                      headers: {
                      'Content-Type': 'application/json;charset=utf-8'
                      }
                  }) 

                  .then(function (response) {
                      if (response.status !== 200) {
                          console.log(response.status);
                          return;
                       }

                      response.json().then(function (data){
                          console.log(data)
                          console.log('end')
                          window.location.href = "http://127.0.0.1:5000/rating/" + user_id;
                      })
                  }) 
          
              });       

          })
      });
  };