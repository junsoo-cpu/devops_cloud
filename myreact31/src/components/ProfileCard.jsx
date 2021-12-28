import "./ProfileCard.css";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBars, faStickyNote } from "@fortawesome/free-solid-svg-icons";

function ProfileCard({
  name,
  role,
  facebook_url,
  email,
  profileImage,
  children,
}) {
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
        <img src={profileImage} alt="프로필 이미지" />

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

      <nav className="others">{children}</nav>
    </section>
  );
}

export default ProfileCard;
