<template>
    <div class="container">
        <div class="image-container">
            <ul class="pokemon-list">
                <li name="pikachu" class="pokemon-item"><img src="../assets/pikachu.jpeg" alt="pikachu"></li>
                <li name="bulbasaur" class="pokemon-item"><img src="../assets/bulbasaur.jpeg" alt="bulbasaur"></li>
                <li name="squirtle" class="pokemon-item"><img src="../assets/squirtle.jpeg" alt="squirtle"></li>
                <li name="charmander" class="pokemon-item"><img src="../assets/charmander.jpeg" alt="charmander"></li>
            </ul>
        </div>
        <div class="data-container">
            <div class="data-item name">
                <label for="name">Nombre</label>
                <input type="text" name="name" id="name">
            </div>
            <div class="data-item level1">
                <label for="attack">Ataque</label>
                <input type="text" name="attack" id="atack">
            </div>
            <div class="data-item level1">
                <label for="speed">Velocidad</label>
                <input type="text" name="speed" id="speed">
            </div>
            <div class="data-item level2">
                <label for="defense">Defensa</label>
                <input type="text" name="defense" id="defense">
            </div>
            <div class="data-item level2">
                <label for="hp">Vida</label>
                <input type="text" name="hp" id="hp">
            </div>
            <div class="data-item create">
                <div class="button" type="button">Crear</div>
            </div>
        </div>
    </div>
</template>
