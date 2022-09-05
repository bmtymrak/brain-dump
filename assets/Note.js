import React, {useState} from 'react'

function Note(props){

    return(
        <div>
                
            <p>{props.note.content} - Tags - {props.note.tags.map((tag, index) =>(tag.name))}</p>
        </div>
    )
}

export default Note