const { join, extname, basename } = require('path')
const { readdirSync, renameSync, existsSync, writeFileSync } = require('fs')

let folder = './weapons'

let list = readdirSync(folder)

console.log(list.length)

for(let i of list){
    let ext = extname(i)
    let name = basename(i, ext)

    let newname = name.split('_')[0].toLowerCase()

    if(!existsSync(join(folder, newname+ext))){
	    renameSync(join(folder, i), join(folder, newname+ext))
    }
}

// get folder stuff and craft into JSON
list = readdirSync(folder)
writeFileSync('./weapon_list.json', JSON.stringify(list, null, 4))