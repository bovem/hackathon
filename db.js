const Sequelize = require('sequelize');

const db = new Sequelize(
    'govdocs',
    'devuser',
    'devuser',
    {
        dialect:'mysql',
        host:'localhost'
    }
) 

const Users = db.define('users',{
    id:{
        type: Sequelize.STRING,
        allowNull: false,
        unique: true,
        primaryKey: true
    },
    aadharId: {
        type: Sequelize.STRING,
        allowNull: false,
        unique:true
    }
})

db.sync().then(()=>{
    console.log('db is ready');
})

exports = module.exports = {
    db, Users
}