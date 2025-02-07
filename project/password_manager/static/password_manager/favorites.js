document.addEventListener('DOMContentLoaded', function() {
    const favoriteButtons = document.querySelectorAll('.favorite-btn');
    favoriteButtons.forEach((favoriteButton) => {
        favoriteButton.addEventListener('click', () => {
            let type = favoriteButton.closest('tr').dataset.type; 
            let uuid = favoriteButton.closest('tr').dataset.uuid;
            console.log(type, uuid);
            if (favoriteButton.firstChild.className === 'bi bi-star') {
                favorite(type, uuid);
                favoriteButton.firstChild.className = 'bi bi-star-fill favorite';       
            } else {
                unfavorite(type, uuid);
                favoriteButton.firstChild.className = 'bi bi-star';           
            }
        })

        favoriteButton.parentElement.addEventListener('mouseover', () => {
            favoriteButton.closest('tr').removeAttribute('data-bs-toggle');
            favoriteButton.closest('tr').removeAttribute('href');
        })

        favoriteButton.parentElement.addEventListener('mouseout', () => {
            favoriteButton.closest('tr').setAttribute('data-bs-toggle', 'offcanvas');
            favoriteButton.closest('tr').setAttribute('href', '#offcanvasScrolling');
        })
    })
})

export async function favorite(type, uuid) {
    try {
        const response = await fetch('/favorite', {
            headers: {
                'Content-Type': 'application/json',
            },
            method: 'PATCH',
            body: JSON.stringify({
                type: type,
                uuid: uuid
            }),
            mode: 'same-origin'
        })
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        
        const json = await response.json();
        console.log(json);

        

    } catch (error) {
        console.error(error.message);
    }
}

export async function unfavorite(type, uuid) {
    try {
        const response = await fetch('/unfavorite', {
            headers: {
                'Content-Type': 'application/json',
            },
            method: 'PATCH',
            body: JSON.stringify({
                type: type,
                uuid: uuid
            }),
            mode: 'same-origin'
        })
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        
        const json = await response.json();
        console.log(json);

 

    } catch (error) {
        console.error(error.message);
    }
}
