import "./ProfileCard.css";
import ProfileImage from "./img/member1.jpg";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBars, faStickyNote } from "@fortawesome/free-solid-svg-icons";

function ProfileCard({ name, role, facebook_url, email, changePageName }) {
  return (
    <section>
      <nav className="menu">
        <a href="#">
          <FontAwesomeIcon icon={faBars} />
        </a>
        <a href="#">
          <FontAwesomeIcon icon={faStickyNote} />
        </a>
      </nav>
      <article className="profile">
        <img src={ProfileImage} alt="프로필 이미지" />

        <h1>{name}</h1>
        <h2>{role}</h2>

        <a href="#" className="btnView">
          VIEW MORE
        </a>
      </article>

      <ul class="contact">
        <li>
          <i className="fab fa-facebook-f"></i>
          <span>{facebook_url}</span>
        </li>
        <li>
          <i class="fas fa-envelope-square"></i>
          <span>{email}</span>
        </li>
      </ul>

      <nav className="others">
        <a className="on" onClick={() => changePageName("Anna")}></a>
        <a className="on" onClick={() => changePageName("Alice")}></a>
        <a className="on" onClick={() => changePageName("Dred")}></a>
        <a className="on" onClick={() => changePageName("Davis")}></a>
      </nav>
    </section>
  );
}

export default ProfileCard;
